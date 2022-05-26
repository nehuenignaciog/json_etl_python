


import json
import requests

import matplotlib.pyplot as plt

def fetch():

    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'

    response = requests.get(url)

    dataset_original = response.json()["results"]

    #dataset_original = json.loads(response.text)
   # print (json.dumps(dataset_original,indent = 4))

    print (type(dataset_original))



    dataset_filtrado = [{"price": x["price"], "condition": x["condition"], "currency_id": x["currency_id"]} for x in dataset_original if  x["currency_id"] == "ARS"  ]


    return dataset_filtrado




 


#def transform(dataset, min, max):





if __name__ == "__main__":


    
    dataset = fetch()
    #print (json.dumps(dataset,indent = 4 ))
    #data = transform(dataset, min, max)