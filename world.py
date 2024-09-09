import requests
import folium
import json
import geolocator

# World Data Base
def get_country_data(country_name):
    url = f"https://api.worldbank.org/v2/country?format=json&per_page=1000&q={country_name}"
    response = requests.get(url)
    data = json.loads(response.text)[1]  # Acessando a lista de países
    return data

# Nome do país que deseja visualizar
country = "Minha Localização"

# Dados do país
data = get_country_data(country)

# Extraindo a latitude e longitude do primeiro resultado 
latitude = data[0]['latitude']
longitude = data[0]['longitude']

# Mapa centrado no país
map = folium.Map(location=[latitude, longitude], zoom_start=5)

# Adicionando um marcador no país
folium.Marker([latitude, longitude], popup=country).add_to(map)

# Mapa HTML
map.save("mapa_gabriel.html")