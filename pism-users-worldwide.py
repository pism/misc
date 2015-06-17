#!/usr/bin/env python
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import csv
 
m = Basemap(lon_0=0,
            resolution='l',     # coastline resolution, can be 'l' (low), 'h'
                                # (high) and 'f' (full)
            projection='robin',   # cylindrical equidistant
            )
 
# draw the Blue Marble background (requires PIL, the Python Imaging Library)
m.bluemarble(scale=0.25)
 
with open('pism-users.csv') as f:
    reader = csv.DictReader(f)
    reader.next()  # skip header
    for row in reader:
        x = row['lon']
        y = row['lat']
        name = row['name']
        xoff = float(row['lon_offset'])
        yoff = float(row['lat_offset'])
        x, y = m(x, y)
        plt.plot(x, y, 'o', color='red')
        plt.annotate(name,
                     xy = (x, y),
                     xytext = (xoff, yoff), textcoords = 'offset points',
                     bbox = dict(boxstyle = "round", fc = "white"),
                     arrowprops = dict(arrowstyle = "simple", fc = "white", ec = "none"))

plt.savefig('pism-users.png', bbox_inches='tight', dpi=300)
