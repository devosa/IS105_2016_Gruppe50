''' Spillet ble i første omgang laget for å kunne kjøre på et GUI.
    Det er derfor ikke implementert funksjoner som kan ta input fra brukeren
    for å kunne endre tilstanden i spillet.

    Det er kun opprettet et testklasse for å se at logikken i spillet fungerer
    som den skal. Her ville man bare ha laget funksjoner som kunne ta input fra
    brukeren (r_rawinput) som igjen kalte på de eksisterende metodene, men dette
    ble ikke implementert grunnet dårlig tid, og større ønske om å få til GUI.

    For å se at logikken i spillet fungerer som den skal kjører man test.py
    '''

class State():
    

    def __init__(self):
        stuffToMove = ["chicken", "fox", "man", "bagOfGrains"]

        self.state = [("boatPos", "left"),
                      ("stuffInBoat", []),
                      ("stuffOnLeftSide", stuffToMove),
                      ("stuffOnRightSide", [])]

    def putInBoat(self, name):
        stuffInBoat = self.state[1][1]

        if self.getBoatPosition() == "left":
            stuffOnLeftSide = self.state[2][1]
            stuffOnLeftSide.remove(name)
        else:
            stuffOnRightSide = self.state[3][1]
            stuffOnRightSide.remove(name)

        stuffInBoat.append(name)

    def putOnLand(self, name):
        stuffInBoat = self.state[1][1]

        if self.getBoatPosition() == "left":
            stuffOnLeftSide = self.state[2][1]
            stuffOnLeftSide.append(name)
        else:
            stuffOnRightSide = self.state[3][1]
            stuffOnRightSide.append(name)

        stuffInBoat.remove(name)

    def moveBoat(self):
        if self.getBoatPosition() == "left":
            self.state[0] = ("boatPos", "right")
        else:
            self.state[0] = ("boatPos", "left")

    def getBoatPosition(self):
        return self.state[0][1];

    def getStuffInBoat(self):
        return self.state[1][1]

    def getStuffOnLeftSide(self):
        return self.state[2][1]

    def getStuffOnRightSide(self):
        return self.state[3][1]

    def getState():
        return self.state
