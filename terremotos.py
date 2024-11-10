import requests
import folium 

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"

resp =requests.get(url)
terremotos= resp.json()

m = folium.Map(location=(0, 0), zoom_start= 2)

for terremoto in terremotos["features"]:
    cordenadas = terremoto["geometry"] ["coordinates"]
    lugar = terremoto["properties"] ["place"]
    magnitud = terremoto["properties"] ["mag"]

    folium.Marker(
        location=[cordenadas[1], cordenadas[0]],
        popup= f" Lugar: {lugar}, Magnitud: {magnitud}",
    ).add_to(m)

m.save("terremotos.html")

