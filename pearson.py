import math
import time
xdata=[]
with open('test0.txt','r') as fin:
    for line in fin:
        x=0
        for c in line.strip():
            x=(x*10)+int(c,10)
        xdata.append(x)
print(xdata)
xsum=0
for x in xdata:
    xsum+=x
avg=xsum/len(xdata)
xmeanlist=[]
xclusterlist=[]
print('Enter number of clusters: ')
k=eval(input())
for i in range(k):
    xmeanlist.append(xdata[i])
    xclusterlist.append([])
print(xmeanlist)
print(xclusterlist)
while 1:
    prevxmeans=[]
    for i in range(k):
        prevxmeans.append(xmeanlist[i])
    for i in range(len(xdata)):
        mindist=math.sqrt(((xmeanlist[0]-xdata[i])**2)+((ymeanlist[0]-ydata[i])**2))
        for j in range(k):
            dist=math.sqrt(((xmeanlist[j]-xdata[i])**2)+((ymeanlist[j]-ydata[i])**2))
            if dist<mindist:
                mindist=dist
        for j in range(k):
            dist=math.sqrt(((xmeanlist[j]-xdata[i])**2)+((ymeanlist[j]-ydata[i])**2))
            if dist==mindist:
                xclusterlist[j].append(xdata[i])
                break
    #print(xclusterlist)
    xmeanlist=[]
    for i in range(len(xclusterlist)):
        xsum=0
        for j in range(len(xclusterlist[i])):
            xsum+=xclusterlist[i][j]
        xavg=xsum/len(xclusterlist[i])
        xmeanlist.append(xavg)
    #print('prevxmeans',prevxmeans)
    #print('xmeanlist',xmeanlist)
    finished=1
    for i in range(k):
        if xmeanlist[i]!=prevxmeans[i]:
            finished=0
    if finished==1:
        print('The clusters are:\n')
        for i in range(k):
            print('Cluster ',i,':\n')
            print(xclusterlist[i])
            print("\n")
        break
    else:
        xclusterlist=[]
        for i in range(k):
            xclusterlist.append([])
        
