import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import openpyxl
from fractions import Fraction

def get_exif_data(image_path):
    image = Image.open(image_path)
    image.verify()  # Verify that this is an image file
    exif_data = image._getexif()
    if not exif_data:
        return None
    
    exif = {}
    for tag, value in exif_data.items():
        decoded = TAGS.get(tag, tag)
        exif[decoded] = value
    
    return exif

def get_gps_info(exif_data):
    if 'GPSInfo' not in exif_data:
        return None
    
    gps_info = {}
    for key in exif_data['GPSInfo'].keys():
        decode = GPSTAGS.get(key, key)
        gps_info[decode] = exif_data['GPSInfo'][key]
    
    return gps_info

def convert_to_degress(value):
    d = float(Fraction(value[0]))
    m = float(Fraction(value[1]))
    s = float(Fraction(value[2]))

    return d + (m / 60.0) + (s / 3600.0)

def get_lat_lon(gps_info):
    if not gps_info:
        return None, None
    
    lat = None
    lon = None

    gps_latitude = gps_info.get('GPSLatitude')
    gps_latitude_ref = gps_info.get('GPSLatitudeRef')
    gps_longitude = gps_info.get('GPSLongitude')
    gps_longitude_ref = gps_info.get('GPSLongitudeRef')

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        lat = convert_to_degress(gps_latitude)
        if gps_latitude_ref != 'N':
            lat = 0 - lat

        lon = convert_to_degress(gps_longitude)
        if gps_longitude_ref != 'E':
            lon = 0 - lon

    return lat, lon

def extract_coordinates_from_images(image_paths):
    coordinates = []
    for image_path in image_paths:
        exif_data = get_exif_data(image_path)
        if not exif_data:
            continue
        
        gps_info = get_gps_info(exif_data)
        lat, lon = get_lat_lon(gps_info)
        if lat and lon:
            coordinates.append((image_path, lat, lon))
    
    return coordinates

def save_to_excel(coordinates, output_file):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Image Coordinates"
    ws.append(["Image Path", "Latitude", "Longitude"])

    for coord in coordinates:
        ws.append(coord)
    
    wb.save(output_file)

def main(image_directory, output_file):
    image_extensions = ('.jpg', '.jpeg', '.tiff', '.png')  # Add more extensions if needed
    image_paths = [os.path.join(image_directory, f) for f in os.listdir(image_directory) if f.lower().endswith(image_extensions)]
    
    coordinates = extract_coordinates_from_images(image_paths)
    save_to_excel(coordinates, output_file)
    print(f"Coordinates have been written to {output_file}")

if __name__ == "__main__":
    # Replace with your directory containing images and desired output file name
    image_directory = '/Users/muttakibismoy/GPStoEXCEL/Data'
    output_file = 'output_coordinates.xlsx'
    
    main(image_directory, output_file)
