from api.src.utils import AddressToCrs, PathToTif, TiffTo3D, TargetToMap


class Construct3D:
    def __init__(self, street, city):
        self.street = street
        self.city = city

    def constructor(self):
        target = AddressToCrs(self.street, self.city).to_crs31370()
        tif_file = PathToTif(target[0], target[1]).finding_tif()
        TiffTo3D(target[0], target[1], tif_file).tif_crop()
        return TiffTo3D(target[0], target[1], tif_file).crop_to_3D()

    def map(self):
        targetLL = AddressToCrs(self.street, self.city).to_long_latt()
        return TargetToMap(targetLL[1], targetLL[0]).to_map()


# Construct3D('gouwberg 15', 'arendonck 2370').map()