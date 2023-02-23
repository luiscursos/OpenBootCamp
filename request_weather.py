###   API   ###

import requests

'''
Consejos maps.google.com:

    Escribe las coordenadas de latitud antes que las de longitud.
    Comprueba que el primer número de la coordenada de latitud sea un valor comprendido entre -90 y 90.
    Comprueba que el primer número de la coordenada de longitud sea un valor comprendido entre -180 y 180.

API CALL
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}


latitud -> 38.2723440076808 
longitud -> -3.614707130859141
'''

city = input("Enter a city: ")

# url  = "https://api.openweathermap.org/data/2.5/weather?lat={}&appid=5cbaecb004c675c2645dd8c47b9d9877=metric".format(city)

url_base = "https://api.openweathermap.org/data/2.5/weather?"

api_key = "5cbaecb004c675c2645dd8c47b9d9877"

url = url_base + "appid=" + api_key + "&q=" + city

print(url)

# Enviar a la API la URL con la ciudad para que la analice
res = requests.get(url)

# La informacion recibida por la API este mejor estructurada para maniupularla mejor
data = res.json()



# Definir tres caracteristicas:
#   1 - La temperatura
#   2   La velocidad el viento
#   3   Descripcion general meteorologica
#   4   Latitud & Longitud


# Las 4 variables siguientes contienen diccionarios dentro de diccionarios como valor

temp = data["main"]["temp"]
temp_min = data["main"]["temp_min"]
temp_max = data["main"]["temp_max"]
wind_speed = data["wind"]["speed"]
latitud = data ["coord"]["lat"]
longitud = data ["coord"]["lon"]


# En descripcion el diccionario esta dentro de una lista
# Por eso indicamos el cero

description = data["weather"][0]["description"]


print("Temperature: ", temp)
print("Temperature Minimun: ", temp_min)
print("Temperature Maximum: ", temp_max)
print("Wind speed: ", wind_speed)
print("latitud: ", latitud)
print("longitud: ", longitud)
print("Description: ", description)