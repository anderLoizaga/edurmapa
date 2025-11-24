from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

class Map3D:

    def render(self, dem, color_map):
        x = np.arange(0, dem.shape[1])
        y = np.arange(0, dem.shape[0])
        X, Y = np.meshgrid(x, y)
        Z = dem

        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        ax.plot_surface(X, Y, Z, facecolors=color_map, rstride=1, cstride=1)

        ax.set_title("Terreno 3D")
        plt.show()
