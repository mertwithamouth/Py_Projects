import folium
import pandas

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

fgv=folium.FeatureGroup(name="Volcanoes")

def creating_markers(data,coordinates):
    for i in range(len(data.index)):
        fgv.add_child(folium.CircleMarker(location=coordinates[i],
        popup="Name= %s \n Status= %s" %(data["NAME"][i], data["STATUS"][i]), 
        fill_color=color(data["ELEV"][i]), color=color(data["ELEV"][i]), fill_opacity=0.7))
    return fgv



creating_markers(df,coordinates)

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else "orange" if 10000000 <= x['properties']['POP2005'] <20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
