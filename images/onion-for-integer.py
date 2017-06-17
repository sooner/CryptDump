import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm

font = {
#'family' : 'serif',  
#        'color'  : 'darkred',  
#        'weight' : 'normal',  
        'size'   : 16,  
        }


cmap = plt.get_cmap('Reds')
colors = [cmap(i) for i in np.linspace(0, 1, 3)]

x = range(4)
y11 = [8,8,8,8]
y21 = [8,8,8,8]
y31 = [8,256,0,0]


fig = plt.figure()


xxx=[i for i in np.linspace(0,0.45, 4)]

plt.bar(xxx,y11,0.15,color='b')


xxx=[i for i in np.linspace(0.75,1.2, 4)]

plt.bar(xxx,y21,0.15,color='r')

xxx=[i for i in np.linspace(1.5,1.95, 4)]

plt.bar(xxx,y31,0.15,color='y')


#y2 = [y11, y21, y31]
label = ['Single Thread', 'SMT2', 'SMT4']
# fig = plt.figure(dpi=80)
x = range(4)

count = 0

#for i,color in enumerate(colors, start=0):
#    temp = [m + count / 10 for m in x]
    #plt.bar(temp, y2[i], 0.13, color=color, label=label[i])
#    count = count + 1.3

plt.xticks([m + 0.18 for m in range(3)], ['det-10', 'det-1000', 'ope'])


#plt.ylim(0,2.5)
#plt.xlim(-0.1, 3.5)
plt.legend()

fig.savefig('onion-for-integer.eps')
