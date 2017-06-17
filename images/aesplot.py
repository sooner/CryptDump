import matplotlib.pyplot as plt 

font = {
#'family' : 'serif',  
#        'color'  : 'darkred',  
#        'weight' : 'normal',  
        'size'   : 16,  
        }


def toint(inlist):
    for i in range(len(inlist)):
        inlist[i]=int(inlist[i])

def tofloat(inlist):
    for i in range(len(inlist)):
        inlist[i]=float(inlist[i])


fh=open('newdata.txt')
x=fh.readline()
xs=x.split()
toint(xs)
#print xs

aes_cbc_enc=fh.readline();
aes_cbc_encs=aes_cbc_enc.split()

tofloat(aes_cbc_encs)
#print aes_cbc_encs

aes_cbc_dec=fh.readline()
aes_cbc_decs=aes_cbc_dec.split()

tofloat(aes_cbc_decs)
#print aes_cbc_decs

aes_cmc_enc=fh.readline()
aes_cmc_encs=aes_cmc_enc.split()

tofloat(aes_cmc_encs)
#print aes_cmc_encs

aes_cmc_dec=fh.readline()
aes_cmc_decs=aes_cmc_dec.split()

tofloat(aes_cmc_decs)
#print aes_cmc_decs



  


fig = plt.figure(dpi=400)


y1=[10,13,5,40,30,60,70,12,55,25] 

x1=range(0,10)

x2=range(0,10)
 
y2=[5,8,0,30,20,40,50,10,40,15]

##plt.plot(xs,aes_cbc_encs,label='Frist line',linewidth=3,color='r',marker='o', markerfacecolor='blue',markersize=12) 


plt.plot(xs,aes_cbc_encs,label='aes_cbc_enc',color='r')

plt.plot(xs,aes_cbc_decs,label='aes_cbc_dec',color='b')


plt.plot(xs,aes_cmc_encs,label='aes_cmc_enc',color='g')

plt.plot(xs,aes_cmc_decs,label='aes_cmc_dec',color='y')



plt.xlabel('Number of blocks',fontdict=font)
plt.ylabel('Time in us',fontdict=font)
plt.title('AES algorithm time complexity',fontdict=font)

plt.legend() 
#plt.show()

fig.savefig("aes.eps")





