import gmplot
import pandas as pd

# Load your dataset
df = pd.read_csv('/Users/muttakibismoy/GPStoEXCEL/output.csv')

# Extract latitude and longitude from the dataset
latitudes = df['Latitude'].tolist()
longitudes = df['Longitude'].tolist()

# Create a gmplot object with the center of the map
gmap = gmplot.GoogleMapPlotter(latitudes[0], longitudes[0], 10, apikey='Enter Your GOOGLE MAP API KEY')

# Plot the points on the map
gmap.scatter(latitudes, longitudes, '#FF0000', size=40, marker=True)

# Draw the map to an HTML file
gmap.draw('/Users/muttakibismoy/GPStoEXCEL/map.html')
