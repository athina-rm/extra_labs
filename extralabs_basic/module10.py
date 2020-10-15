#From the list below. Print a sorted list with duplicated removed
#li=[12,24,35,24,88,120,155,88,120,155]

li=[12,24,35,24,88,120,155,88,120,155]
newlist=[]
for x in li:
   if x not in newlist:
       newlist.append(x)
#for i in range (0,len(newlist)):
#    for j in range (i+1,len(newlist)):
#        if newlist[i]>newlist[j]:
#            x=newlist[i]
#            newlist[i]=newlist[j]
#            newlist[j]=x
newlist.sort()
print(newlist)

