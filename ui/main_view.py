class MainView:

    def __init__(self, tile_manager, terrain, control):
        self.tile_manager = tile_manager
        self.terrain = terrain
        self.control = control

    def update(self, lat, lon):
        dem, transform = self.tile_manager.load_tile(lat, lon)
        slope = self.terrain.compute_slope(dem)
        aspect = self.terrain.compute_aspect(dem)
        orient = self.terrain.classify_orientation(aspect)

        return dem, slope, orient
