import folium
import pandas
import random

map=folium.Map(location=[40.76, -73.98], zoom_start=15,tiles="Stamen Terrain")


df=pandas.read_csv("Volcanoes.txt")
lat=list(df["LAT"])
lon=list(df["LON"])

coordinates=[]
for lat,lon in zip(lat,lon):
    coordinates.append([lat,lon])


def color(high):
    if high <1000:
        return "green"
    elif 1000<= high <3000:
        return "orange"
    else:
        return "red"

fg=folium.FeatureGroup(name="My Map")

def creating_markers(data,coordinates):
    for i in range(len(data.index)):
        fg.add_child(folium.CircleMarker(location=coordinates[i],
        popup="Name= %s \n Status= %s" %(data["NAME"][i], data["STATUS"][i]), 
        fill_color=color(data["ELEV"][i]), color=color(data["ELEV"][i]), fill_opacity=0.7))
    return fg

creating_markers(df,coordinates)

map.add_child(fg)

map.save("Map1.html")
