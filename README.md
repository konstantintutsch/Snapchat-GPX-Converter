# Snapchat Data Export GPX Converter

Convert your Snapchat location history from a data export to a GPX file for better oversight.

## Requesting data

Request a data download at [accounts.snapchat.com](https://accounts.snapchat.com/v2/download-my-data) or within the settings of the Snapchat app. Make sure to enable the “Export JSON Files” and “Ranking And Location” options!

Once you have been informed that your export is ready, download and unpack it.

## Usage

All location data tracked by Snapchat is stored in `./json/location_history.json`.

```
locations-to-gpx.py ./json/location_history.json
```

Your GPX file is now available at `./json/location_history.json.gpx`.
