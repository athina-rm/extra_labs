#3. Create a Pets class that holds instances of dogs; this class is completely separate from the
#Dog class. In other words, the Dog class does not inherit from the Pets class. Then assign three
#dog instances to an instance of the Pets class
#Your output should look like
#I have 3 dogs.
#Tom is 6.
#Fletcher is 7.
#Larry is 9. 

class Pets():
    def __init__(self,dogs=[]):
        self._dogs=dogs

    def addDog(self,dog):
        self._dogs.append(dog)

    def getNoofDogs(self):
        return len(self._dogs)

    def getdog(self):
        return self._dogs

class Dog():
    def __init__ (self,dog_name, dog_age):
        self._dog_name=dog_name
        self._dog_age=dog_age

    def getDogName(self):
        return self._dog_name

    def getDogAge(self):
        return self._dog_age

myDogs=Pets()
dog1=Dog("Tom",6)
dog2=Dog("Fletcher",7)
dog3=Dog("Larry",9)
myDogs.addDog(dog1)
myDogs.addDog(dog2)
myDogs.addDog(dog3)
print(f"I have {myDogs.getNoofDogs()} dogs")
for dog in myDogs.getdog():
    print(f"{dog.getDogName()} is {dog.getDogAge()}")


