# Find
#Find all occurrences of “USA” in given string ignoring the case

string=input("Enter the string : ")
count=0

count=string.lower().count('usa')
if count==0:
    print('"USA" is not found in the entered string')
else:
    print(f'"USA" is found {count} times')

