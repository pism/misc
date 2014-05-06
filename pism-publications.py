#!/usr/bin/env python
#
# (C) 2014 Andy Aschwanden
#
# XKCD-style plot of pism publications per year.

import numpy as np
import pylab as plt

year, no_of_pubs = np.loadtxt('pism-publications.csv', delimiter=',', skiprows=1, dtype=int,  unpack=True)


bar_width = 0.5
plt.xkcd(scale=1, length=100, randomness=1)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.bar(year + bar_width/2, no_of_pubs, bar_width, color='#C6DBEF', edgecolor='#3182BD', linewidth=2.5)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ymax = np.max(no_of_pubs) + 1
ax.set_ylim([0, ymax])
plt.xlabel('year')
plt.xticks(year + bar_width, year)
plt.title('Number of PISM publications')

plt.tight_layout()


plt.savefig('pism-publications.pdf', bbox_inches='tight')
plt.savefig('pism-publications.png', bbox_inches='tight')
