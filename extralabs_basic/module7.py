# Accept string from the user and display only those characters which are present at an even
#index
#Enter String pynative
#Orginal String is pynative
#Printing only even index chars
#index[ 0 ] p
#index[ 2 ] n
#index[ 4 ] t
#index[ 6 ] v

string=input("Enter the String:")
for i in range(0,len(string)-1,2):
    print(f"index[{i}] {string[i]}")

