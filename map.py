import folium
import pandas as pd


def main():
    df=pd.read_csv('transformed_data.csv')

    m = folium.Map(location=(28.0339,1.6596))

    for index, item in df.iterrows():
        folium.Marker(location=[item["latitude"],item["longtitude"]],popup=item["temperature"]).add_to(m)

    m.save("TempPrint.html")