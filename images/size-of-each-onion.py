import numpy as np
import matplotlib.pyplot as plt

N = 5
men_means = (20, 251, 20,34,7.7)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()

### How we find document Axes.bar(left, height, width=0.8, bottom=None, **kwargs)
###  bars : matplotlib.container.BarContainer
rects1 = ax.bar(ind, men_means, width, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('length')
ax.set_xlabel('layers')

ax.set_title('Length of each layers')

ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('IV','HOM', 'DET', 'OPE', 'PLAIN'))

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)

plt.show()