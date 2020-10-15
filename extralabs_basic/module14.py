from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, personummer,name):
        self._personnummer=personummer
        self._name=name

    def setName(self,name):
        self.name=name

    def getName(self):
        return self._name

    @abstractmethod
    def calculateSalary(self):
        pass

class Boss(Person):
    #def __init__ (self,personummer,name):
    #    super().__init__(personummer,name)
        

    def calculateSalary(self):
        return 100000

class Worker(Person):
    #def __init__ (self,personummer,name):
    #        super().__init__(personummer,name)
            

    def calculateSalary(self):
        return 5000

myboss=Boss(688888801,"Stefan")
worker1=Worker(68913801,"Hui")
worker2=Worker(68218031,"Joe")
employees=[myboss,worker1,worker2]
for i in employees:
    print(i.getName(),":",i.calculateSalary())
        
