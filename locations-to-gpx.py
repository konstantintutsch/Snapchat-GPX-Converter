#!/usr/bin/env python

import sys, json
from datetime import datetime

path = sys.argv[1]
gpx = path + ".gpx"

if not path:
    print("No JSON file path given")
    exit(1)

indent = "    "

# XML (GPX) header
contents = ['<?xml version="1.0" encoding="UTF-8"?>\n']
contents += ['<gpx version="1.0">\n']
contents += [indent + '<name>' + "Snapmap (location data export)" + '</name>\n']
contents += [indent + '<trk><name>' + '</name><number>1</number><trkseg>\n']

# JSON conversion
file = open(path, "r")
data = json.load(file)

for location in data['Location History']:
    time = datetime.strptime(location[0], "%Y-%m-%d %H:%M:%S %Z").isoformat()

    # location[1]: "lat ± acc, lon ± acc"
    lat = location[1].split(',')[0].split(' ')[0]
    lon = location[1].split(", ")[1].split(' ')[0]

    print("You were at " + lat + ", " + lon + " on " + time)
    contents += [indent + indent + '<trkpt lat="' + lat + '" lon="' + lon + '">\n']
    contents += [indent + indent + indent + '<time>' + time + '</time>\n']
    contents += [indent + indent + '</trkpt>\n']

# GPX End
contents += [indent + '</trkseg></trk>\n']
contents += ['</gpx>\n']

# Write
write = open(gpx, "w")
write.writelines(contents)
write.close()
