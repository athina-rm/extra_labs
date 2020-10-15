#Skriv ett program som simulerar två tärningskast (random). Du ska skriva ut en bra text på vad det
#blev:
#en sexa och en tvåa.
#Men blir det två av samma ska du skriva
#två treor
import random
while True:
    dieChoices=["ett","två", "tre", "fyra", "fem", "sex"]
    die1= random.choice(dieChoices)
    die2= random.choice(dieChoices)

    if die1==die2:
        print(f"två {die2}or")
    else:
        print(f"en {die1}a och en {die2}a")