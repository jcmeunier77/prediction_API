import shapefile
from shapely.geometry import Point, Polygon


class PathToTif:
    number_tif = [x for x in range(9, 10)]

    def __init__(self, xtarget, ytarget):
        self.xtarget = xtarget
        self.ytarget = ytarget
        self.shp = ""
        self.dsm_path = ""

    def target_to_point(self):
        return Point(self.xtarget, self.ytarget)

    @staticmethod
    def bbox_to_polygon(box):
        return Polygon([[box[0], box[1]], [box[0], box[3]],
                        [box[2], box[3]], [box[2], box[1]]])

    def finding_tif(self):
        for i in self.number_tif:
            self.shp = shapefile.Reader(f'api/src/data/DSM_vlaanderen/DHMVIIDSMRAS1m_k{i:02}/DHMVII_vdc_k{i:02}/DHMVII_vdc_k{i:02}.shp')
            shp_polygon = self.bbox_to_polygon(self.shp.bbox)
            target_point = self.target_to_point()
            if shp_polygon.contains(target_point):
                # code for the normal tif file
                #                self.dsm_path = f'api/src/data/DSM_vlaanderen/DHMVIIDSMRAS1m_k{i:02}/GeoTIFF/DHMVIIDSMRAS1m_k{i:02}.tif'
                # code for the reduced tif file
                #                 self.dsm_path = f'api/src/data/DSM_vlaanderen/DHMVIIDSMRAS1m_k{i:02}/GeoTIFF/arendonk_k{i:02}.tif'
                # code for the smaller reduced tif file
                self.dsm_path = f'api/src/data/DSM_vlaanderen/DHMVIIDSMRAS1m_k{i:02}/GeoTIFF/arendonk_small_k{i:02}.tif'
            else:
                pass
        return self.dsm_path


#print(PathToTif(199414.11, 223588.55).finding_tif())
