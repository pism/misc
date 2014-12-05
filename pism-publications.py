#!/usr/bin/env python
#
# (C) 2014 Andy Aschwanden
#
# XKCD-style plot of pism publications per year.

import numpy as np
import pylab as plt

year, no_of_pubs, no_of_uaf_pubs = np.loadtxt('pism-publications.csv', delimiter=',', skiprows=1, 
               dtype=int,  unpack=True)

bar_width = 0.5
plt.xkcd(scale=1, length=100, randomness=1)


### bar graph with total pubs in different color ###
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.bar(year + bar_width/2, no_of_pubs, bar_width, 
       color='#C6DBEF', edgecolor='#3182BD', linewidth=2.5)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ymax = np.max(no_of_pubs) + 1
ax.set_ylim([0, ymax])
plt.xlabel('year')
plt.xticks(year + bar_width, year, fontsize=20.0)
plt.yticks(fontsize=20.0)
plt.title('Number of PISM publications')

plt.tight_layout()

plt.savefig('pism-publications.png', bbox_inches='tight')


### bar graph with UAF pubs in different color ###
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.bar(year + bar_width/2, no_of_pubs, bar_width, 
       color='#C6DBEF', edgecolor='#3182BD', linewidth=2.5)
ax.bar(year + bar_width/2, no_of_uaf_pubs, bar_width, 
       color='#FFEA00', edgecolor='#FFD500', linewidth=2.5)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ymax = np.max(no_of_pubs) + 1
ax.set_ylim([0, ymax])
plt.xlabel('year')
plt.xticks(year + bar_width, year, fontsize=20.0)
plt.yticks(fontsize=20.0)
plt.title('Number of PISM publications\nyellow = has UAF (co-)authors')

plt.tight_layout()

plt.savefig('pism-uaf-publications.png', bbox_inches='tight')
