import argparse
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


def tides_csv_to_geojson(input_csv, output_geojson):
    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(input_csv)

    # Convert latitude and longitude into geometry points
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]

    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame(df, geometry=geometry)

    # Save to GeoJSON file
    gdf.to_file(output_geojson, driver="GeoJSON")

    print(f"GeoJSON data has been written to {output_geojson}")


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Convert TIDES vehicle locations CSV to GeoJSON.")

    # Input CSV file
    parser.add_argument(
        'input_csv',
        type=str,
        help='Path to the input CSV file containing vehicle locations'
    )

    # Output GeoJSON file
    parser.add_argument(
        'output_geojson',
        type=str,
        help='Path to save the output GeoJSON file'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Call the conversion function with the provided file paths
    tides_csv_to_geojson(args.input_csv, args.output_geojson)


if __name__ == "__main__":
    main()
