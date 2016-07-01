#!/usr/bin/env python
#
# (C) 2014 Andy Aschwanden
#
# XKCD-style plot of pism publications per year.

import numpy as np
import pylab as plt

def saveit(filename):
    print 'writing image %s' % filename
    plt.savefig(filename, bbox_inches='tight')

def startit():
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    return ax

def completeit(ax,year,ymax,xtickoffset):
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_ylim([0, ymax])
    ax.set_xlim([np.min(year), np.max(year)+1.0])
    plt.xlabel('year')
    plt.xticks(year + xtickoffset, year, fontsize=16.0)
    plt.yticks(fontsize=20.0)
    plt.title('Number of PISM publications')
    plt.tight_layout()

year, no_of_pubs, no_of_uaf_pubs = np.loadtxt('pism-publications.csv', delimiter=',', skiprows=1, 
               dtype=int,  unpack=True)

plt.xkcd(scale=1, length=100, randomness=1)
bar_width = 0.5

### bar graph with total pubs ###
ax = startit()
ax.bar(year + bar_width/2, no_of_pubs, bar_width, 
       color='#C6DBEF', edgecolor='#3182BD', linewidth=2.5)
completeit(ax,year,np.max(no_of_pubs) + 1,bar_width)
saveit('pism-publications.png')

### bar graph with UAF pubs in different color ###
ax = startit()
ax.bar(year + bar_width/2, no_of_pubs, bar_width, 
       color='#C6DBEF', edgecolor='#3182BD', linewidth=2.5)
ax.bar(year + bar_width/2, no_of_uaf_pubs, bar_width, 
       color='#FFEA00', edgecolor='#FFD500', linewidth=2.5)
completeit(ax,year,np.max(no_of_pubs) + 1,bar_width)
plt.text(2007.5,4.0,'yellow\n= UAF (co-)authors')
saveit('pism-uaf-publications.png')

