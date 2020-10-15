#Skapa en array och generera 100 slump-tal som du lägger i arrayen.
#Visa hur man kan ta fram medelvärde av alla tal som är jämnt delbara med 3 och som finns i
#arrayen.
import random
Numlist=random.sample(range(1000000),100)

for i in Numlist:
    print (i)

total=0
count=0

for i in Numlist:
    if i%3==0:
        total+=i
        count+=1
print(total/count)
