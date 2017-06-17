import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm

cmap = plt.get_cmap('Reds')

colors = [cmap(i) for i in np.linspace(0, 1, 3)]

x = range(4)
y11 = [10,16,32,48]

y21 = [1000,1008,1024,1040]

y31 = [10,8,16,32]

fig = plt.figure()
ax = fig.add_subplot(111)


xxx=[i for i in np.linspace(0,0.45, 4)]

b1 = ax.bar(xxx,y11,0.15,color='b',label='DET-STR for strlen=10')


b2 = xxx=[i for i in np.linspace(0.75,1.2,4)]

ax.bar(xxx,y21,0.15,color='r',label='DET-STR for strlen=1000')

b3 = xxx=[i for i in np.linspace(1.5,1.95, 4)]
ax.bar(xxx,y31,0.15,color='g',label='DET-OPE')


#for i,color in enumerate(colors, start=0):
#    temp = [m + count / 10 for m in x]
    #plt.bar(temp, y2[i], 0.13, color=color, label=label[i])
#    count = count + 1.3


#plt.xticks([m*0.15 + 0 for m in range(4)], ['Plain', 'DET-JOIN-STR', 'DET-STR','DET-RND'],rotation=45)

#plt.xticks([m*0.15 + 0.75 for m in range(4)], ['Plain', 'DET-JOIN-STR', 'DET-STR','DET-RND'],rotation=45)

#plt.xticks([m*0.15 + 1.5 for m in range(4)], ['Plain', 'OPE-JOIN-STR', 'OPE-STR','OPE-RND'],rotation=45)



plt.ylim(0,1500)
#plt.xlim(-0.1, 3.5)
#ax.legend((b1,b2,b3),('DET-STR for strlen=10','DET-STR for strlen=1000','DET-OPE'))

fig.savefig('onions-for-string.eps')


