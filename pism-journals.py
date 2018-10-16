#!/usr/bin/env python
#
# (C) 2018 Ed Bueler
#
# bar plot of pism publications versus journal impact factor

import numpy as np
import matplotlib.pyplot as plt
import csv

jrcsv = 'journal-rank.csv'
ajcsv = 'author-journal.csv'

jif = {}   # dictionary:  jif[initials] = [jif,count]
print('reading %s' % jrcsv)
with open(jrcsv) as cfile:
    creader = csv.reader(cfile, delimiter=',')
    line_count = 0
    for row in creader:
        if line_count == 0:
            print('  column names: %s' % ",".join(row))
            line_count += 1
        else:
            #print('JIF for %s is %g' % (row[0],float(row[1])))
            line_count += 1
            jif[row[0]] = [float(row[1]),0]
    print('  processed %d items.' % (line_count-1))
jif['other'] = [0.0,0]

print('reading %s' % ajcsv)
with open(ajcsv) as cfile:
    creader = csv.reader(cfile, delimiter=',')
    line_count = 0
    for row in creader:
        if line_count == 0:
            print('  column names: %s' % ",".join(row))
            line_count += 1
        elif row:
            #print('%s appeared in %s which has JIF %g' % (row[0],row[1],jif[row[1]][0]))
            jif[row[1]][1] += 1
            line_count += 1
    print('  processed %d items.' % (line_count-1))
#print(jif)

# sort and remove cases with only one such pub (they go in singles bar)
jif_sort = sorted(jif.items(), key=lambda x: x[1])
initials = map(lambda x: x[0], jif_sort)
initials[0] = 'singles'
initials = np.array(initials, dtype=str)
frequency = np.array(map(lambda x: x[1][1], jif_sort))
#print(initials)
#print(frequency)
frequency[0] += sum(frequency == 1)
initials = initials[frequency > 1]
frequency = frequency[frequency > 1]

# bar graph with jif on x-axis, pubs on y
plt.clf()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
bar_width = 0.5
xx = range(len(frequency))
ax.grid(axis='y')
ax.bar(xx, frequency, bar_width, linewidth=2.5, color='#a63603')
ax.set_yticks(np.linspace(0,20,5))
ax.set_ylabel('number of PISM publications')
ax.set_xlabel(r'increasing 2018 Journal Impact Factor $\to$',fontsize=14.0)
ax.set_xticks(xx)
ax.set_xticklabels(initials, style='italic')
ticklabels = ax.get_xticklabels()
for tick in ticklabels:
    tick.set_rotation(80)

# save figure
filename = 'pism-journals.png'
print 'writing image %s' % filename
plt.savefig(filename, bbox_inches='tight')

