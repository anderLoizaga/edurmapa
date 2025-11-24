import numpy as np

class ColorSchemes:

    @staticmethod
    def altitude_map(dem):
        dem_norm = (dem - np.min(dem)) / (np.max(dem) - np.min(dem))
        return dem_norm

    @staticmethod
    def slope_map(slope):
        slope_norm = slope / np.max(slope)
        return slope_norm

    @staticmethod
    def orientation_map(orientation):
        cmap = {
            0: [0, 0, 1],   # Norte → Azul
            1: [0, 1, 0],   # Este → Verde
            2: [1, 0, 0],   # Sur → Rojo
            3: [1, 1, 0],   # Oeste → Amarillo
        }

        color_image = np.zeros((orientation.shape[0], orientation.shape[1], 3))
        for code, color in cmap.items():
            color_image[orientation == code] = color
        return color_image
