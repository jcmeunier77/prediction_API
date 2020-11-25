from api.src.utils import EstimPrice


class LaunchEstim:
    def __init__(self, building, Postalcode, house_area, surf_land, numb_facades, numb_rooms, garden, terrace,
                     terrace_area, equip_kitch, fire, pool, Sas_new, Sjust_renov,
                     Sgood, Sto_refresh, Sto_renov, Sto_restor):
        """
        json format:
        variables = {"building":"house/apartment", "Postalcode":"7830", "house_area":196, "surf_land":125,"numb_facades":4, "numb_rooms":3, "garden":True,
         "terrace":False, "terrace_area":10, "equip_kitch":True, "fire":True, "pool":True, "Sas_new":True, "Sjust_renov":False,
         "Sgood":False, "Sto_refresh":False, "Sto_renov":False, "Sto_restor":False}
        """
        self.building = building
        self.Postalcode = Postalcode
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

    def go_estim(self):
        if self.building=="house":
            return EstimPrice(self.Postalcode, self.house_area, self.surf_land, self.numb_facades, self.numb_rooms,
                              self.garden, self.terrace, self.terrace_area, self.equip_kitch, self.fire, self.pool,
                              self.Sas_new, self.Sjust_renov, self.Sgood, self.Sto_refresh, self.Sto_renov,
                              self.Sto_restor).house_price()
        elif self.building=="apartment":
            return EstimPrice(self.Postalcode, self.house_area, self.surf_land, self.numb_facades, self.numb_rooms,
                              self.garden, self.terrace, self.terrace_area, self.equip_kitch, self.fire, self.pool,
                              self.Sas_new, self.Sjust_renov, self.Sgood, self.Sto_refresh, self.Sto_renov,
                              self.Sto_restor).apart_price()
        else:
            return 'Building type should be "House" or "Apartment"'