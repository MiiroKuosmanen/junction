import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import requests
text_file = open("ean_codes.txt", "r")
ean_set_new = text_file.read().split(',')
ean_set_new = [x.strip() for x in ean_set_new]
ean_set_new = [int(x) for x in ean_set_new]
ean_set_new = [json.dumps(ean) for ean in ean_set_new]

"""get the product data for list of csv EAN-codes
    and writes the products into txt files in JSON format""" 

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9a94c5afb6a34bed810db27ae4f1fbd8',
}

params = urllib.parse.urlencode({})
temp = 0
"""We got all of the product information from 140 000 EAN-codes
    to !!!!!!make some fake profiles of people!!!!!!!!"""
    
for i in range(100, 140000, 100):
    eans = ean_set_new[temp:i]
    body = dict(filters=dict(ean=eans))
    r = requests.post("https://kesko.azure-api.net/v1/search/products", headers=headers, json=body)
    file = "products{}.txt".format(i)
    
    with open(file, "w") as outfile:
        json.dump(r.json(), outfile)
    outfile.close()
    temp += 100
