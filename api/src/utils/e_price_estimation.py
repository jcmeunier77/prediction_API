import numpy as np
import pickle
import json

"""
json format : 
{"building":"house/apartment", "Postalcode":"7830", "house_area":125, "surf_land":125,"numb_facades":4, "numb_rooms":3, "garden":True, 
 "terrace":False, "terrace_area":10, "equip_kitch":True, "fire":True, "pool":True, "Sas_new":True, "Sjust_renov":False,
 "Sgood":False, "Sto_refresh":False, "Sto_renov":False, "Sto_restor":False}
"""
with open('api/src/data/Dict_cp_rank/CP_to_city.json', 'r') as fcp:
    cp_to_city = json.load(fcp)
with open('api/src/data/Dict_cp_rank/City_to_rank.json', 'r') as fci:
    city_to_rank = json.load(fci)


class EstimPrice:

    def __init__(self, Postalcode, house_area, surf_land, numb_facades, numb_rooms, garden, terrace,
                 terrace_area, equip_kitch, fire, pool, Sas_new, Sjust_renov,
                 Sgood, Sto_refresh, Sto_renov, Sto_restor):
        self.Postalcode = Postalcode
        self.city = cp_to_city['Commune principale'][str(self.Postalcode)]
        self.rank = city_to_rank[str(self.city)]
        self.house_area = house_area
        self.surf_land = surf_land
        self.numb_facades = numb_facades
        self.numb_rooms = numb_rooms
        self.garden = garden
        self.terrace = terrace
        self.terrace_area = terrace_area
        self.equip_kitch = equip_kitch
        self.fire = fire
        self.pool = pool
        self.Sas_new = Sas_new
        self.Sjust_renov = Sjust_renov
        self.Sgood = Sgood
        self.Sto_refresh = Sto_refresh
        self.Sto_renov = Sto_renov
        self.Sto_restor = Sto_restor

    def house_price(self):
        features = np.array([[self.rank, self.rank ** 2, self.rank ** 3, self.house_area, self.surf_land,
                              self.numb_facades, self.numb_rooms, self.garden, self.terrace, self.terrace_area,
                              self.equip_kitch, self.fire, self.pool, self.Sas_new, self.Sjust_renov, self.Sgood,
                              self.Sto_refresh, self.Sto_renov, self.Sto_restor]])
        House_model = pickle.load(open('api/src/data/ML_models/House_regression', 'rb'))
        return {"estimated_price":str(House_model.predict(features)[0])}

    def apart_price(self):
        features = np.array(
            [[self.rank, self.rank ** 2, self.rank ** 3, self.house_area, self.numb_rooms, self.terrace,
              self.terrace_area, self.equip_kitch, self.fire, self.Sas_new, self.Sjust_renov, self.Sgood,
              self.Sto_refresh, self.Sto_renov, self.Sto_restor]])
        Apart_model = pickle.load(open('api/src/data/ML_models/Apart_regression', 'rb'))
        return {"estimated_price":str(Apart_model.predict(features)[0])}

#EstimPrice(7850, 99, 2, 0, 0, 1, 0, 1,0,0,0,0,0).apart_price()
