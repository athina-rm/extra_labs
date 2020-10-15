#Mid string
#Given a string of odd length greater 7, return a string made of the middle three chars of a
#given String
#Original String is JhonDipPeta
#Middle three chars are Dip

def midString(string):
    if len(string)>7 and len(string)%2==1:
        middle=int((len(string)+1)/2)
        midstring=string[middle-2:middle+1]
        return(midstring)
    return None

string=input("Enter  a string :")
print(midString(string))