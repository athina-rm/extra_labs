#. Given a two list. Create a third list by picking an odd-index element from the first list and
#even index elements from second.
#listOne = [3, 6, 9, 12, 15, 18, 21]
#listTwo = [4, 8, 12, 16, 20, 24, 28]


listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
newList=[]
for j in range (0,len(listTwo),2):
    newList.append(listTwo[j])
for i in range(1, len(listOne),2):
    newList.insert(i,listOne[i])
print(newList)