# Programmera HANGMAN spelet
#Här är ett exempel på hur dialogen mellan användaren och datorn kan se ut.
#Den som ska spela måste titta bort nu!
#Skriv in ett ord: Hammare
#(skärmen rensas…)
#Ord: _ _ _ _ _ _ _
#Gissa en bokstav eller ordet? E
#Bra! Du har 6 gissningar kvar.
#Ord: _ _ _ _ _ _ E
#Gissa en bokstav? A
#Ord: _ A _ _ A _ E
#Bra! Du har 6 gissningar kvar.
#Gissa en bokstav eller ordet? N
#Ord: _ A _ _ A _ E
#Missar: N
#Fel! Du har 5 gissningar kvar.
#Gissa en bokstav eller ordet? r
#Ord: _ A _ _ A R E
#Missar: N
#Rätt! Du har 5 gissningar kvar.
#Gissa en bokstav eller ordet? Tattare
#Ord: _ A _ _ A R E
#Missar: N
#Fel ord! Du har 4 gissningar kvar.
#Gissa en bokstav eller ordet? n
#Ord: _ A _ _ A R E
#Missar: N
#Du har redan försökt med N! Du har 4 gissningar kvar.
#OBS: Håll reda på redan gjorda ”Du har redan försökt med N”

import os
import time

def draw(count):
    if count==0:
        print("+--+")
        print("|  ")
        print("|   ")
        print("|   ")
        print("|\  ")
    if count==1:
        print("+--+")
        print("|  o")
        print("|   ")
        print("|   ")
        print("|\  ")
    elif count==2:
        print("+--+")
        print("|  o")
        print("|  |")
        print("|   ")
        print("|\  ")
    elif count==3:
        print("+--+")
        print("|  o")
        print("| /|")
        print("|   ")
        print("|\  ")
    elif count==4:
        print("+--+")
        print("|  o")
        print("| /|\\")
        print("|   ")
        print("|\  ")
    elif count==5:
        print("+--+")
        print("|  o")
        print("| /|\\")
        print("| / ")
        print("|\ ")
    elif count==6:
        print("+--+")
        print("|  o")
        print("| /|\\")
        print("| / \\")
        print("|\  ")

word=input("Enter a word:")
userWord=[]
word_in_array=[]
for i in range (0,len(word)):
    userWord.append("_")
    word_in_array.append(word[i])
chanceCount=len(word)
missCount=0
wordcopy=word
charList=[]
while chanceCount>0:
    os.system('cls')
    draw(missCount)
    print(f"You have {chanceCount} more guesses left" ) 
    print("WORD:",*userWord)
    char =input("Guess the word or an alphabet :")    
    if char in charList:
        print(f"You already tried '{char}'")
        time.sleep(1.5)
    else:
        charList.append(char)
        chanceCount-=1
        count=word.count(char)
        if char not in word:
            print(f"Its a miss!!:'{char}'")
            missCount+=1
            #draw(missCount)
            time.sleep(1.5)
        else:
            for j in range(0,count):            
                index=word.find(char)
                word=word.replace(char,"_",1)
                userWord[index]=char
            print(f"Good!!")
            time.sleep(1.5)
        if word_in_array==userWord or char==wordcopy:
            os.system('cls')
            print("WORD:",*wordcopy)
            print("Congratulations!! You got the word.")
            break
        elif word_in_array!=userWord and chanceCount==0:
            os.system('cls')
            draw(missCount)
            print("Sorry!! You have no more guesses left")
            print("WORD:",*userWord)
            print("GAME OVER!!")




