# get_data.py
import requests
import json


if __name__=="__main__":
    print("REQUESTING SOME DATA FROM THE INTERNET...")
    request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
    
    response = requests.get(request_url)
    response_data = json.loads(response.text)
    
    print(response_data['name'])

    request2_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"

    resp = requests.get(request2_url)
    resp_data = json.loads(resp.text)

    #print(type(resp_data))
    i = 0
    
    while i != len(resp_data):
        print('Name:',resp_data[i]['name'],' ','ID:',resp_data[i]['id'])
        i = i + 1
