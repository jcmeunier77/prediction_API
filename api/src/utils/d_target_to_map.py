import folium

class TargetToMap:

# targetLL = 51.319986, 5.077554
    def __init__(self, target_lon, target_lat):
        self.target = [target_lon, target_lat]
        self.target_lat = target_lat

    def to_map(self):
        mappy = folium.Map(location=[self.target[0],self.target[1]], zoom_start=60)
        folium.CircleMarker(location=[self.target[0],self.target[1]], radius=30, popup='Your address', color='#3186cc',
                            fill=True, fill_color='#3186cc').add_to(mappy)
        mappy.save('./templates/map.html')
        return mappy
# print(TargetToMap(51.319986, 5.077554).to_map())
