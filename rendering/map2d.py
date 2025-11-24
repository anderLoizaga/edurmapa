import matplotlib.pyplot as plt

class Map2D:

    def __init__(self):
        pass

    def render(self, image, title="Mapa 2D"):
        plt.figure(figsize=(6,6))
        plt.imshow(image)
        plt.axis("off")
        plt.title(title)
        plt.show()
