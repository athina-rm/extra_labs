class HockeyTeam():
    def __init__(self,TeamName,city):
        self._players=[]
        self._TeamName=TeamName
        self._city=city

    def addPlayer(self,player):
        self._players.append(player)

class hockeyPlayer():
    def __init__(self,name,jerseyno,age):
        self._name=name
        self._jerseyno=jerseyno
        self._age=age

myTeam=HockeyTeam("AIK","Solna")
player1=hockeyPlayer("Mats Thelin",2,50)
player2=hockeyPlayer("Per-Erik Eklund",12,50)
myTeam.addPlayer(player1)
myTeam.addPlayer(player2)