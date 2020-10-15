#Gör saamma sak fast med TRE tärninigar. Se till att svensk syntax blir rätt med ”och” osv
#Det blev en tvåa, en sexa och en femma
#Det blev två fyror och en trea
#Det blev tre femmor

import random
while True:
    dieChoices=["ett","två", "tre", "fyra", "fem", "sex"]
    die1= random.choice(dieChoices)
    die2= random.choice(dieChoices)
    die3= random.choice(dieChoices)
    #diceNumbers=[die1,die2,die3]

    if die1==die2==die3:
        print(f"tre {die2}or")
    elif die1==die2 :
        print (f"två {die1}or och en {die3}a")
    elif die1==die3:
        print (f"två {die1}or och en {die2}a")
    elif die2==die3:
        print (f"två {die2}or och en {die1}a")
    else:
        print(f"en {die1}a, en {die2}a och en {die3}a")


