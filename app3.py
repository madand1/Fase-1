# Bibliotecas necesarias
import requests
import json
import os
from dotenv import load_dotenv

# Variables de entorno desde el archivo dotenv.env
load_dotenv(dotenv_path="dotenv.env")

# Guardamos la url base
url_base="https://api.themoviedb.org/3/"

# Variable KEY
key=os.environ["api_key"]

# Código del país, en esta caso Inglaterra
code='en-US'

# Diccionario que guarde nuestros parámetros
payload = {'api_key':key,"languaje":code}

# Peticion de titulo 
serie = input("Introduce el nombre de la serie o tv show que desea buscar: ")


url = url_base+'search/tv'+'?query='+serie
r=requests.get(url,params=payload)


if r.status_code == 200:
    doc=r.json()
    
    print(json.dumps(doc, indent=4, sort_keys=True))
else:
    print ("Error")
    print (r.status_code)
