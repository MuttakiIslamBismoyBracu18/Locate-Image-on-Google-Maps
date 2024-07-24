
# GMPlot

## Description
This script plots GPS coordinates from a CSV file onto a Google Map and saves the map as an HTML file. It uses the `gmplot` library to create the map and `pandas` to handle the CSV file.

## Prerequisites
- Python 3.x
- A Google Maps API key

## Installation
1. Ensure Python 3 is installed on your machine.
2. Install the required Python packages using the provided `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Place your CSV file with GPS coordinates in a directory.
2. Update the `df = pd.read_csv('/path/to/your/csvfile.csv')` line in the script to point to your CSV file.
3. Replace `'YOUR_GOOGLE_MAPS_API_KEY'` with your actual Google Maps API key in the script.
4. Run the script:
   ```
   python GMPlot.py
   ```
5. The script will generate an HTML file named `map.html` with the plotted GPS data.

## Script Details
- `gmplot.GoogleMapPlotter(lat, lng, zoom, apikey='YOUR_GOOGLE_MAPS_API_KEY')`: Initializes the gmplot object with the center of the map and the API key.
- `gmap.scatter(latitudes, longitudes, color, size, marker)`: Plots the points on the map.
- `gmap.draw('path/to/map.html')`: Draws the map to an HTML file.

## Example
1. Ensure your CSV file is in the specified directory.
2. Update the script with the correct path to your CSV file and your Google Maps API key.
3. Run the script.
4. Open the generated `map.html` file in a web browser to view the map.

## Dependencies
- gmplot
- pandas

## License
This project is licensed under the MIT License - see the LICENSE file for details.
