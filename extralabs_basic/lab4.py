#4. Skapa lite klasser för ett spel:
#En basklass som heter GameObject (x och y -koordinater)
#Denna ska inte gå att instansiera.
#Den ska ha en metod Draw som alla subclasser måste implementera.
#Skapa Rocket som ärver från GameObject.
#Skapa också en enemyklass som ärver från GameObject.
#Skapa upp några objekt, lägg i en lista och loopa igenom och "rita ut"
#på skärmen (dvs kör Draw)
from abc import ABC, abstractmethod

class gameObject(ABC):
    def __init__(self,x_axis, y_axis):
        self._x_axis=x_axis
        self._y_axis=y_axis
    
    @abstractmethod
    def draw(self):
        pass
class Rocket(gameObject):
    pass
class Enemy(gameObject):
    pass