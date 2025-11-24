import os
from .dem_loader import DEMLoader

class TileManager:
    def __init__(self, base_path="DEM/"):
        self.base_path = base_path
        self.cache = {}

    def coords_to_tile(self, lat, lon):
        lat_floor = int(lat)
        lon_floor = int(lon)
        return f"{lat_floor}N_{abs(lon_floor)}{'W' if lon < 0 else 'E'}.tif"

    def load_tile(self, lat, lon):
        tile_name = self.coords_to_tile(lat, lon)
        tile_path = os.path.join(self.base_path, tile_name)

        if tile_name in self.cache:
            return self.cache[tile_name]

        loader = DEMLoader(tile_path)
        dem, transform = loader.load_dem()
        self.cache[tile_name] = (dem, transform)

        return dem, transform
