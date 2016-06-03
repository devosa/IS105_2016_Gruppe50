import numpy as np
import matplotlib.pyplot as plt

N = 6
menMeans = (3546, 2380, 3606, 3976, 2410, 2774)
menStd = (0, 0, 0, 0, 0, 0)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

womenMeans = (266, 183, 262, 364, 187, 215)
womenStd = (0, 0, 0, 0, 0, 0)
rects2 = ax.bar(ind + width, womenMeans, width, color='y', yerr=womenStd)

# add some text for labels, title and axes ticks
ax.set_ylabel('MiliSeconds')
ax.set_title('Search Results Group 50')
ax.set_xticks(ind + width)
ax.set_xticklabels(('Svenn', 'Oscar', 'Erlend', 'Dan-Marius', 'Vegard', 'Anders'))

ax.legend((rects1[0], rects2[0]), ('Search_slow', 'Search_fast'))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()