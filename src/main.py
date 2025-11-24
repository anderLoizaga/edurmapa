from core.tile_manager import TileManager
from core.terrain_analysis import TerrainAnalysis
from rendering.color_schemes import ColorSchemes
from rendering.map2d import Map2D
from rendering.map3d import Map3D
from ui.control_panel import ControlPanel
from ui.main_view import MainView

def main():

    tile_manager = TileManager("DEM/ESP/")
    terrain = TerrainAnalysis()
    control = ControlPanel()
    view = MainView(tile_manager, terrain, control)

    # Zona de Pirineos ejemplo
    lat, lon = 42.7, 0.5

    dem, slope, orient = view.update(lat, lon)

    if control.show_altitude:
        alt_img = ColorSchemes.altitude_map(dem)
        Map2D().render(alt_img, "Altitud")

    if control.show_slope:
        slope_img = ColorSchemes.slope_map(slope)
        Map2D().render(slope_img, "Pendiente")

    if control.show_orientation:
        orient_img = ColorSchemes.orientation_map(orient)
        Map2D().render(orient_img, "Orientación")

    if control.view_3d:
        color = ColorSchemes.altitude_map(dem)
        Map3D().render(dem, color)

if __name__ == "__main__":
    main()
