# Importamos las bibliotecas necesarias
import requests
import json
import os
from dotenv import load_dotenv

# Cargamos las variables de entorno desde el archivo dotenv.env
load_dotenv(dotenv_path="dotenv.env")

# Guardamos la URL base
url_base = "https://api.themoviedb.org/3/"

# Obtener la clave API de mi entorno
api_key = os.getenv("API_KEY")

# Error si no esta la clave API
if api_key is None:
    print("Error: No se encontró la clave de la API en el archivo dotenv.env.")
    exit()

# Código del país, en este caso Inglaterra
country_code = os.getenv("COUNTRY_CODE", "EN")

# Pedir la ID de la película
movie_id = input("Introduce la ID de la película: ")

# URL con los parámetros
url = f"{url_base}movie/{movie_id}"
payload = {'api_key': api_key, 'countryCode': country_code}
response = requests.get(url, params=payload)

# Guardamos en una variable el contenido de la respuesta
if response.status_code == 200:
   
    movie_data = response.json()
    
    print(json.dumps(movie_data, indent=4, sort_keys=True))
else:
    
    print("Error:", response.status_code)
