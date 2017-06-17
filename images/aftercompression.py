import numpy as np
import matplotlib.pyplot as plt

font = {
#'family' : 'serif',  
#        'color'  : 'darkred',  
#        'weight' : 'normal',  
        'size'   : 16,  
        }

N = 4
men_means = (20.0, 20.0, 50.0, 34.0)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, men_means, width, color='r')

women_means = (9.4, 0.046, 49.0, 0.097)

rects2 = ax.bar(ind + width, women_means, width, color='y')


# add some text for labels, title and axes ticks
ax.set_xlabel('Layer', fontdict=font )
ax.set_ylabel('Size in MB', fontdict=font )

ax.set_title('After compression', fontdict=font )
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('RND_INT', 'DET_INT', 'RND_STR', 'DET_STR'),fontdict=font )

ax.legend((rects1[0], rects2[0]), ('Before compression', 'After compression'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.3f' % height,
                ha='center', va='bottom', fontdict=font )

autolabel(rects1)
autolabel(rects2)

plt.ylim(0,60)
#plt.xlim(-0.1, 3.5)


#plt.show()

fig.savefig('aftercompression.eps')
