import numpy as np

class TerrainAnalysis:

    @staticmethod
    def compute_slope(dem):
        gy, gx = np.gradient(dem)
        slope = np.sqrt(gx**2 + gy**2)
        slope_deg = np.degrees(np.arctan(slope))
        return slope_deg

    @staticmethod
    def compute_aspect(dem):
        gy, gx = np.gradient(dem)
        aspect = np.degrees(np.arctan2(-gx, gy))
        aspect = (aspect + 360) % 360
        return aspect

    @staticmethod
    def classify_orientation(aspect):
        orientation = np.zeros_like(aspect, dtype=int)

        orientation[(aspect >= 315) | (aspect < 45)] = 0   # Norte
        orientation[(aspect >= 45) & (aspect < 135)] = 1   # Este
        orientation[(aspect >= 135) & (aspect < 225)] = 2  # Sur
        orientation[(aspect >= 225) & (aspect < 315)] = 3  # Oeste

        return orientation
