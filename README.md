# Snapchat Data Export GPX Converter

Convert your Snapchat location history from their data exports to a GPX file for better oversight.

## Usage

How to use this script.

### Request data

Request a data download at [accounts.snapchat.com](https://accounts.snapchat.com/v2/download-my-data) or within the settings of the Snapchat app.

Make sure to enable the “Export JSON Files” and “Ranking And Location” options!

Once you have been informed that your export is ready, download and unpack it.

### Script

All location data tracked by Snapchat is stored in `./json/location_history.json`.

Convert it to `./json/location_history.json.gpx`:

```
locations-to-gpx.py ./json/location_history.json
```
