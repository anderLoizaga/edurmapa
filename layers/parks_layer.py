import geopandas as gpd

class ParksLayer:
    def __init__(self, filepath):
        self.data = gpd.read_file(filepath)

    def get_polygons(self):
        return self.data
