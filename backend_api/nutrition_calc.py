import pandas as pd
import requests
import json
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9a94c5afb6a34bed810db27ae4f1fbd8',
}

params = urllib.parse.urlencode({})

nutrition_codes = []
                
date_test = ['2017-01-01','2017-01-02','2017-01-03']

def nutrition_calc(data, dates):
    #TODO multiply calories by weight
    """Calculates the average nutrition intake per day for one person
        returns the info in a dictionary
        :param data: csv file that contains the persons purchase history
        :param dates: list that contains the dates for the purchases. Example_dates = ['2017-01-01','2017-01-02','2017-01-03']"""
        
    df = pd.read_csv(data)
    df = df.loc[df['TransactionDate'].isin(dates)]
    df = df['EAN']
    temp = 0
    list = []
    nutritions = {}
    for ean in df:
        list.append(ean)
    list = [json.dumps(ean) for ean in list]

    for i in range(500, 20000, 500):    #loop for sending requests for 500 EAN codes at a time.
        list = list[temp:i]
        body = dict(filters=dict(ean=list))
        r = requests.post("https://kesko.azure-api.net/v1/search/products", headers=headers, json=body)
        r = r.json()
        for x in range(0, 501):     #loop for retrieving product attributes
            try:
                item = r["results"][x]['attributes']
                for key in nutrition_codes:
                    try:
                        value = item[key]['value']['value']
                        try:
                            nutritions[key] += (float(value) / len(dates))
                        except KeyError:
                            nutritions[key] = (float(value) / len(dates))
                    except (KeyError, TypeError):
                        pass
            except IndexError:
                break
        temp += 500
    return nutritions
    
if __name__ == "__main__":
    print(nutrition_calc("customers_0_4.csv", date_test))
