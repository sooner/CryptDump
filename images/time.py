import numpy as np
import matplotlib.pyplot as plt

font = {
#'family' : 'serif',  
#        'color'  : 'darkred',  
#        'weight' : 'normal',  
        'size'   : 16,  
        }

N = 3
men_means = (0.12, 4454.21, 143.76)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, men_means, width, color='r')

women_means = (0.11, 382.44, 140.07)

rects2 = ax.bar(ind + width, women_means, width, color='y')


# add some text for labels, title and axes ticks
ax.set_xlabel('Layer',fontdict=font)
ax.set_ylabel('Size in MB',fontdict=font)

ax.set_title('After compression',fontdict=font)
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('Blowfish', 'HOM', 'OPE'),fontdict=font)

ax.legend((rects1[0], rects2[0]), ('Encryption', 'Decryption'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.3f' % height,
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.ylim(0,10000)
#plt.xlim(-0.1, 3.5)


#plt.show()

fig.savefig('time.eps')
