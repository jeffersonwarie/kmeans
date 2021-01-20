import math
import time
xdata=[]
ydata=[]
with open('test.txt','r') as fin:
    for line in fin:
        x=y=0
        comma=0
        for c in line.strip():
            if c==',' and comma==0:
                comma=1
            elif comma==1:
                y=(y*10)+int(c,10)
            else:
                x=(x*10)+int(c,10)
        xdata.append(x)
        ydata.append(y)
print(xdata)
print(ydata)
xmeanlist=[]
ymeanlist=[]
xclusterlist=[]
yclusterlist=[]
print('Enter number of clusters: ')
k=eval(input())
for i in range(k):
    xmeanlist.append(xdata[i])
    ymeanlist.append(ydata[i])
    xclusterlist.append([])
    yclusterlist.append([])
print(xmeanlist)
print(ymeanlist)
print(xclusterlist)
print(yclusterlist)
while 1:
    prevxmeans=[]
    prevymeans=[]
    for i in range(k):
        prevxmeans.append(xmeanlist[i])
        prevymeans.append(ymeanlist[i])
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
                yclusterlist[j].append(ydata[i])
                break
    #print(xclusterlist)
    #print(yclusterlist)
    xmeanlist=[]
    ymeanlist=[]
    for i in range(len(xclusterlist)):
        xsum=ysum=0
        for j in range(len(xclusterlist[i])):
            xsum+=xclusterlist[i][j]
            ysum+=yclusterlist[i][j]
        xavg=xsum/len(xclusterlist[i])
        yavg=ysum/len(yclusterlist[i])
        xmeanlist.append(xavg)
        ymeanlist.append(yavg)
    #print('prevxmeans',prevxmeans)
    #print('prevymeans',prevymeans)
    #print('xmeanlist',xmeanlist)
    #print('ymeanlist',ymeanlist)
    finished=1
    for i in range(k):
        if xmeanlist[i]!=prevxmeans[i] or ymeanlist[i]!=prevymeans[i]:
            finished=0
    if finished==1:
        print('The clusters are:\n')
        for i in range(k):
            print('Cluster ',i,':\n')
            print(xclusterlist[i])
            print(yclusterlist[i])
            print("\n")
        break
    else:
        xclusterlist=[]
        yclusterlist=[]
        for i in range(k):
            xclusterlist.append([])
            yclusterlist.append([])
        
