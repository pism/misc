#!/usr/bin/env python
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
 
m = Basemap(lon_0=0,
            resolution='l',     # coastline resolution, can be 'l' (low), 'h'
                                # (high) and 'f' (full)
            projection='robin',   # cylindrical equidistant
            )
 
# draw the Blue Marble background (requires PIL, the Python Imaging Library)
m.bluemarble(scale=0.25)
 
# label, point location, label offset
users = {"UAF"    : [(65, -148), (10,  20)],  # Univ of Alaska, Fairbanks
         "VUW"    : [(-41, 175), (20, -10)],  # Antarctic Res Centre, Victoria Univ, Wellington
         "DMI"    : [(56, 13),   (25,  10)],  # Danish Meteorological Inst
         "CIC"    : [(56, 13),   (0,   40)],    # Centre for Ice and Climate, Univ Copenhagen
         "PIK"    : [(52, 13),   (-20, 20)],  # Potsdam Inst for Climate Impact Res
         "IMAU"   : [(52, 5),    (-40,  0)], # Inst for Marine and Atmospheric Res, Utrecht, NL
         "INK"    : [(59, 18),   (20,  40)],   # INK, Stockholm Univ, Sweden
         "MPI"    : [(54, 10),   (30, -15)],  # Max Planck Inst for Meteorology
         "DUR"    : [(55, -2),   (-15,-45)], # Durham Univ, UK
         "CAM"    : [(52, 0),    (-30,-30)], # University of Cambridge, UK
         "UIB"    : [(60, 5),    (20, -40)],  # University of Bergen, Norway
         "UNBC"   : [(54, -123), (-5, -60)],   # University of Northern British Columbia
         "UW"     : [(47, -122), (-20, -40)],   # University of Washington
         "Yale"   : [(41.31, -72.93),  (-85, -30)],   # Yale
         "UMaine" : [(45, -69),  (18, -10)],   # University of Maine
         "ETH"    : [(47, 8.5),  (-60, -30)],   # ETH Zurich
         "AWI"    : [(53.5, 8.5),  (-15, 60)],   # AWI Bremerhaven
         "Harvard"    : [(42.37, -71.12),  (-65, -10)],   # Harvard
         "Dickinson"    : [(47,-77),  (-50, -100)],   # Dickinson
         "UNSW"   : [(-34,151),  (-30,-40)], # University of New South Wales
         "LSU"    : [(30,-91),   (-30,    -10)], # Louisiana State University
         "UI"     : [(64, -22), (15, -40)],    # University of Iceland
         "PKU"   : [(39.91, 116.40),  (-35, -20)],   # Peking University
         "UC"     : [(42, -87.6), (-15, -40)],        # University of Chicago
         }
 
for name in users.keys():
    y, x = users[name][0]
    x, y = m(x, y)
    ytext, xtext = users[name][1]
    plt.plot(x, y, 'o', color='red')
    plt.annotate(name,
                 xy = (x, y),
                 xytext = (xtext, ytext), textcoords = 'offset points',
                 bbox = dict(boxstyle = "round", fc = "white"),
                 arrowprops = dict(arrowstyle = "simple", fc = "white", ec = "none"))

plt.savefig('pism-users.png', bbox_inches='tight', dpi=300)
