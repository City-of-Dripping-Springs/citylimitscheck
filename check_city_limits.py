import requests

# ArcGIS API Configuration
ARC_GIS_URL = "https://cods.maps.arcgis.com/arcgis/rest/services/DrippingSpringsBoundary/FeatureServer/0/query"

# Function to query ArcGIS API to check if an address is within the city limits
def check_city_limits_arcgis(latitude, longitude):
    """
    Check if the provided latitude and longitude fall within the city limits of Dripping Springs, Texas.

    Args:
        latitude (float): Latitude of the address.
        longitude (float): Longitude of the address.

    Returns:
        bool: True if the address is within the city limits, False otherwise.
    """
    params = {
        "geometry": f"{longitude},{latitude}",
        "geometryType": "esriGeometryPoint",
        "spatialRel": "esriSpatialRelIntersects",
        "inSR": "4326",  # Spatial reference WGS 84
        "outFields": "*",
        "returnGeometry": "false",
        "f": "json"
    }
    response = requests.get(ARC_GIS_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return bool(data["features"])  # True if intersects with Dripping Springs boundary
    else:
        raise Exception(f"ArcGIS API Error: {response.status_code} - {response.text}")

# Main script
def main():
    print("Welcome to the Dripping Springs Address Checker!")

    # Collect user input for coordinates
    try:
        latitude = float(input("Enter Latitude (e.g., 30.1905): "))
        longitude = float(input("Enter Longitude (e.g., -98.0867): "))
    except ValueError:
        print("Invalid input. Please enter valid numeric coordinates for latitude and longitude.")
        return

    try:
        print("Checking city limits with ArcGIS...")
        if check_city_limits_arcgis(latitude, longitude):
            print("The address is within the corporate city limits of Dripping Springs, Texas.")
        else:
            print("The address is NOT within the corporate city limits of Dripping Springs, Texas.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
