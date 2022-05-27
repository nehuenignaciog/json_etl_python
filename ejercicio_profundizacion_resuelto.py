import json
from typing_extensions import dataclass_transform
import requests

import matplotlib.pyplot as plt

def fetch(ciudad):

    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20{}%20&limit=50'.format(ciudad)

   
    response = requests.get(url)

    dataset_original = response.json()["results"]

    dataset_filtrado = [{"price": x["price"], "condition": x["condition"], "currency_id": x["currency_id"]} for x in dataset_original if  x["currency_id"] == "ARS"  ]

    return dataset_filtrado






def transform(dataset, min, max):

    dataset_min = [{"price": x["price"], "condition": x["condition"], "currency_id": x["currency_id"]} for x in dataset if   x["price"] <= min ]
    dataset_min_max = [{"price": x["price"], "condition": x["condition"], "currency_id": x["currency_id"]} for x in dataset if  x["price"] <= max and  x["price"] >= min ]
    dataset_max = [{"price": x["price"], "condition": x["condition"], "currency_id": x["currency_id"]} for x in dataset if  x["price"] >= max  ]

    min_count = len(dataset_min)   
    min_max_count = len(dataset_min_max)  
    max_count = len(dataset_max)

    dataset_used = [{"price": x["price"], "condition": x["condition"], "currency_id": x["currency_id"]} for x in dataset if  x["condition"] == "used"  ]
    dataset_new = [{"price": x["price"], "condition": x["condition"], "currency_id": x["currency_id"]} for x in dataset if  x["condition"] == "new"  ] 
    dataset_na = [{"price": x["price"], "condition": x["condition"], "currency_id": x["currency_id"]} for x in dataset if  x["condition"] == "not_specified"  ]

    used_count = len(dataset_used)    
    new_count = len(dataset_new)    
    na_count = len(dataset_na)



    return [min_count, min_max_count, max_count, used_count, new_count, na_count]


    

def report(data, min, max,ciudad):
    


    precio = ["Precio < {} ".format(min), " {} <= Precio <= {} ".format(min, max), "{} < Precio".format(max)]

    count_departamentos = [data[0], data[1], data[2]]


    #Grafico 1
    fig = plt.figure()
    fig.suptitle('Ubicación: {}'.format(ciudad),fontsize = 18, color = '#7C99AC')
    ax = fig.add_subplot()
    
    ax.bar(precio,count_departamentos, label =  'Cantidad de Departamentos' , color = '#8FBDD3')
    ax.set_facecolor('#f0efeb')
    ax.set_xlabel("Referencia de precios")
    
    ax.legend()
    ax.grid()
    #plt.xticks(precio)
    #plt.yticks(count_departamentos)
    
    
    
    #Grafico 2

    fig2 = plt.figure()
    fig2.suptitle('Ubicación: {}'.format(ciudad),fontsize = 18, color = '#7C99AC')
    estado = ["Usados", "Nuevos", "No especificado"]
    count_new_used = [data[3], data[4], data[5]]

    ax2 = fig2.add_subplot()

    ax2.pie(count_new_used, labels = estado, colors = ['#68A7AD', '#AC7D88', '#E2DEA9'])
    ax2.set_facecolor('#f0efeb')
    ax2.set_xlabel("Estado de Departamentos")
    
    ax2.legend()
    ax2.grid()
    
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":

    min =15000
    max = 35000
    ciudad ="Capital Federal"
    
    dataset = fetch(ciudad)
    data = transform(dataset, min, max)
    report(data,min,max,ciudad)
    