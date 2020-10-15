#Write a program (function!) that takes a list and returns a new list that contains all the
#elements of the first list minus all the duplicates.

def delDuplicates(list):
    newlist=[]
    for i in list:
        if i not in newlist:
            newlist.append(i)
    return newlist
list=[23,78,34,67,89,54,23,34]
newlist=delDuplicates(list)
print (newlist)