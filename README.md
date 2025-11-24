# EduRMapa - Educational Terrain Mapping Tool

A Python application for visualizing and analyzing digital elevation models (DEM) with interactive 2D and 3D terrain mapping capabilities.

## Features

- Load and process Digital Elevation Model (DEM) data
- Generate terrain analysis maps (altitude, slope, orientation)
- 2D and 3D terrain visualization
- Support for multiple data layers (IGN, parks)
- Interactive control panel for customizing views

## Prerequisites

- Python 3.10+
- pipenv (for dependency management)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/anderLoizaga/edurmapa.git
cd edurmapa
```

### 2. Install Dependencies

This project uses `pipenv` for dependency management. If you don't have pipenv installed:

```bash
# Install pipenv
pip install pipenv
```

Then install the project dependencies:

```bash
# Install all dependencies
pipenv install

# Or install with development dependencies
pipenv install --dev
```

### 3. Data Setup

The application requires DEM (Digital Elevation Model) data files. Create the required directory structure:

```bash
mkdir -p DEM/ESP/
```

You'll need to provide DEM files in TIFF format in the `DEM/ESP/` directory. The application expects files named in the format `{lat}N_{lon}E.tif` (e.g., `42N_0E.tif`).

**Note**: DEM data files are not included in this repository due to their size. You can obtain DEM data from sources like:
- [USGS Earth Explorer](https://earthexplorer.usgs.gov/)
- [European Environment Agency](https://www.eea.europa.eu/)
- [NASA SRTM](https://www2.jpl.nasa.gov/srtm/)

## Usage

### Running the Application

```bash
# Activate the virtual environment and run
pipenv run python main.py
```

### Example Usage

The application is currently configured to display terrain data for the Pyrenees region (coordinates: 42.7°N, 0.5°E).

### Project Structure

```
edurmapa/
├── main.py                 # Main application entry point
├── Pipfile                 # Project dependencies
├── core/                   # Core functionality
│   ├── dem_loader.py      # DEM data loading
│   ├── terrain_analysis.py # Terrain analysis algorithms
│   └── tile_manager.py    # Tile management
├── layers/                 # Data layers
│   ├── ign_layer.py       # IGN (National Geographic Institute) layer
│   └── parks_layer.py     # Parks layer
├── rendering/             # Visualization components
│   ├── color_schemes.py   # Color mapping schemes
│   ├── map2d.py          # 2D map rendering
│   └── map3d.py          # 3D map rendering
└── ui/                    # User interface
    ├── control_panel.py   # Control panel interface
    └── main_view.py       # Main view controller
```

## Dependencies

### Core Dependencies
- **numpy**: Numerical computing
- **matplotlib**: Plotting and visualization
- **rasterio**: Geospatial raster data I/O
- **geopandas**: Geospatial data manipulation
- **pyproj**: Cartographic projections and coordinate transformations
- **shapely**: Geometric objects manipulation
- **pillow**: Image processing
- **gpxpy**: GPX file processing
- **fastkml**: KML file processing

### Development Dependencies
- **black**: Code formatting
- **flake8**: Code linting
- **ipython**: Enhanced interactive Python shell

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'numpy'**
   ```bash
   pipenv install numpy
   ```

2. **DEM file not found error**
   - Ensure you have placed DEM files in the `DEM/ESP/` directory
   - Check that file names match the expected format (e.g., `42N_0E.tif`)

3. **Virtual environment issues**
   ```bash
   # Remove and recreate the virtual environment
   pipenv --rm
   pipenv install
   ```

## Development

### Setting up Development Environment

```bash
# Install development dependencies
pipenv install --dev

# Activate the virtual environment
pipenv shell

# Run linting
flake8 .

# Format code
black .
```

### Running Tests

Currently, no tests are implemented. This would be a good area for contribution.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source. Please add a license file as appropriate.

## Contact

- GitHub: [@anderLoizaga](https://github.com/anderLoizaga)
- Repository: [edurmapa](https://github.com/anderLoizaga/edurmapa)