import rasterio
import numpy as np

class DEMLoader:
    def __init__(self, tile_path):
        self.tile_path = tile_path

    def load_dem(self):
        with rasterio.open(self.tile_path) as src:
            dem = src.read(1).astype(float)
            transform = src.transform
        return dem, transform
