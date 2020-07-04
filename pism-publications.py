#!/usr/bin/env python3
#
# (C) 2014--2020 Andy Aschwanden, Ed Bueler
#
# XKCD-style plot of pism publications per year.

import numpy as np
import pylab as plt


def saveit(filename):
    print("writing image {}".format(filename))
    plt.savefig(filename, bbox_inches="tight")


def startit():
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    return ax


def completeit(ax, year, ymax, xtickoffset):
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    ax.set_ylim([0, ymax])
    ax.set_xlim([np.min(year), np.max(year) + 1.0])
    plt.xlabel("year", fontsize=16)
    plt.xticks(year + xtickoffset, year, fontsize=16.0)
    plt.yticks(np.arange(0, ymax + 1, 3), fontsize=16.0)
    plt.tight_layout()


year, no_of_pubs, no_of_uaf_pubs, no_of_aa_pubs = np.loadtxt(
    "pism-publications.csv", delimiter=",", skiprows=1, dtype=int, unpack=True
)
bar_width = 0.5

### bar graph with AA pubs
ax = startit()
ax.bar(year + bar_width / 2, no_of_aa_pubs, bar_width, color="#cbc9e2", edgecolor="#54278f", linewidth=2.5)
completeit(ax, year, np.max(no_of_aa_pubs) + 2, bar_width)
ax.fill_between([0, 2009], [0, 0], [8, 8], color="0.9")
ax.fill_between([2009, 2014], [0, 0], [8, 8], color="0.7")
ax.fill_between([2014, 2018], [0, 0], [8, 8], color="0.5")
ax.fill_between([2018, 2020], [0, 0], [8, 8], color="0.3")
ax.vlines([2009, 2014, 2018], 0, 8)
plt.text(2004.5, 6.25, "PhD student\nETH", fontsize=18)
plt.text(2009.5, 6.25, "Post-doc\nUAF", fontsize=18)
plt.text(2014.5, 6.25, "Asst. Prof.\nUAF", fontsize=18)
plt.text(2019.5, 6.25, "Assoc. Prof.\nUAF", fontsize=18)
plt.title("Number of publications (%d so far)" % sum(no_of_aa_pubs), fontsize=18)
ax.set_xlim(2004.5)
ticklabels = ax.get_xticklabels()
for tick in ticklabels:
    tick.set_rotation(90)
saveit("aschwanden-publications.png")

# remove zero years at start
no_of_pubs = no_of_pubs[year >= 2007]
no_of_uaf_pubs = no_of_uaf_pubs[year >= 2007]
year = year[year >= 2007]

### bar graph with UAF pubs in different color ###
ax = startit()
ax.bar(year + bar_width / 2, no_of_pubs, bar_width, color="#bdd7e7", edgecolor="#3182BD", linewidth=2.5)
ax.bar(year + bar_width / 2, no_of_uaf_pubs, bar_width, color="#fdbe85", edgecolor="#a63603", linewidth=2.5)
completeit(ax, year, np.max(no_of_pubs) + 1, bar_width)
plt.text(2007.5, 15.0, "orange\n= UAF (co-)authors", fontsize=18)
plt.title("Number of PISM publications (%d so far)" % sum(no_of_pubs), fontsize=18)
ticklabels = ax.get_xticklabels()
for tick in ticklabels:
    tick.set_rotation(90)
saveit("pism-uaf-publications.png")

### bar graph with total pubs ###
plt.xkcd(scale=1, length=100, randomness=1)
ax = startit()
ax.bar(year + bar_width / 2, no_of_pubs, bar_width, color="#C6DBEF", edgecolor="#3182BD", linewidth=2.5)
completeit(ax, year, np.max(no_of_pubs) + 1, bar_width)
plt.title("Number of PISM publications (%d so far)" % sum(no_of_pubs))
ticklabels = ax.get_xticklabels()
for tick in ticklabels:
    tick.set_rotation(90)
saveit("pism-publications.png")
