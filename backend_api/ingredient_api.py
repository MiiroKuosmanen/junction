import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
import json


import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9a94c5afb6a34bed810db27ae4f1fbd8',
}

nutrition_codes = ['ENERKJ', 'AVITAM', 'B12VIT', 'B6VITA', 'BIOTII',
                    'CVITAM', 'DVITAM', 'EVITAM', 'ENERKC','ALKPI' , 'FLUORI', 'FOOLIH',
                    'FOSFOR', 'HIHYDR', 'HIHYSO', 'HIHYTA', 'JODI', 'KALIUM', 'KALSIU', 'KLORID',
                    'KOSTPI', 'KROMI', 'KUPARI', 'KUIVPI', 'KUITUA', 'KVITAM', 'LAKTOO', 'LIHAPI',
                    'MAGNES', 'MANGAA', 'MAITPI', 'MARJPI', 'MELAIS', 'MOLYB', 'NATPIT', 'NIASIN',
                    'PANTOT', 'PROTEG', 'RAAPAI', 'RASKTY', 'RASMTY', 'RASVAA', 'RASVPI', 'RAUTAA',
                    'SELEEN', 'SINKKI', 'SOKEPI', 'SOKERI', 'SUKLPI', 'SUOLA', 'SUOLPI',
                    'TAMEPI', 'TIAMII', 'TYYDPI', 'TYYDRH']

list = ['13205', '5548', '7077', '5350', '6031']

def recipes_nutrition_values(id):
    """nutrition values for the recipe
       :param list id: list of ingredientTypes (for example ['7068', '7182']
       :return dictionary containing nutrition attributes and their values"""
    #TODO multiple nutritional values by the amount that actually gets put into the recipe
    array_of_objects = [{"name" : "ingredientType",
                        "value": id,
                        "operator": "or"
                        }]
    nutritions = {}                    
    array_of_objects = json.dumps(array_of_objects)
    body = dict(filters=array_of_objects)
    r = requests.post("https://kesko.azure-api.net/v1/search/products", headers=headers, json=body)
    items = r.json()
    items = items["results"]
    for ingredient in items:
        for key in nutrition_codes:
            try:
                value = ingredient["attributes"][key]['value']['value']
                try:
                    nutritions[key] += float(value)
                except KeyError:
                    nutritions[key] = float(value)
            except (KeyError, TypeError):
                pass
    return nutritions
    
if __name__ == "__main__":
    print(recipes_nutrition_values(list))