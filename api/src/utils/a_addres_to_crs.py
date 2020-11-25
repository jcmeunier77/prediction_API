from geopy.geocoders import GoogleV3
from pyproj import Transformer

locator = GoogleV3(api_key="AIzaSyACSuQBDhEU_qREpV4NevzKn0bi_W4ra0E")


class AddressToCrs:
    def __init__(self, street, city):
        self.street = street
        self.city = city
        self.locator = locator
        self.toll = self.locator.geocode(f"{self.street}, {self.city}, Belgique")
        self.transformer = Transformer.from_crs(4326, 31370)
        self.target = self.transformer.transform(self.toll.latitude, self.toll.longitude)

    def to_long_latt(self):
        return self.toll.longitude, self.toll.latitude

    def to_crs31370(self):
        return self.target


#print(AddressToCrs('Rue de la station 34', '7830 Silly').to_long_latt())

