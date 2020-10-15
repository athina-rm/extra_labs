# Password validator:
#Skriv en funktion som tar ett lösenord som inparameter.
#Den ska returnera true eller false beroende på om lösenordet uppfyller
#följande krav:
#minst 8 tecken
#minst en stor bokstav
#minst en liten bokstav
#minst en siffra

import string

def passwordValidator(pwd):
    if len(pwd)>7:
        for i in pwd:
            if i in string.ascii_lowercase:
                for i in pwd:
                    if i in string.ascii_uppercase:
                        for i in pwd:
                            if i in string.digits:
                                return True
    return False
pwd=input("enter password : ")
print(passwordValidator(pwd))



