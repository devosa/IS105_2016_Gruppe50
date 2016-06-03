from sm import State

class RiverGame():
    def __init__(self):
        self.state = State()

    def play(self):
        self.getGameStatus()

    def moveBoat(self):
        # validate that man is in boat
#        self.validateLand(name)
#        self.validateBoat(name)

        self.state.moveBoat()
        self.getGameStatus()

    def putInBoat(self, name):
        self.validateBoat(name)
        self.validateLand(name)

        self.state.putInBoat(name)

    def putOnLand(self, name):
        self.validateLand(name)
        self.validateBoat(name)

        self.state.putOnLand(name)

    def validateBoat(self, name):
        stuffInBoatList = self.state.getStuffInBoat()

        if name == "chicken":
            if ("fox" in stuffInBoatList) or ("bagOfGrains" in stuffInBoatList):
                if not "man" in stuffInBoatList:
                    print "Game over"
        elif name == "fox":
            if "chicken" in stuffInBoatList:
                if not "man" in stuffInBoatList:
                    print "Game over"

        elif name == "bagOfGrains":
            if "chicken" in stuffInBoatList:
                if not "man" in stuffInBoatList:
                    print "Game over"


    def validateLand(self, name):
        stuffInBoatList = self.state.getStuffInBoat()
        stuffOnLandList = self.state.getStuffOnRightSide()

        boatPos = self.state.getBoatPosition()
        if boatPos == "left":
            stuffOnLandList = self.state.getStuffOnLeftSide()

        if name != "chicken":
            if name == "fox":
                if ("chicken" in stuffOnLandList) and ("bagOfGrains" in stuffOnLandList) and ("man" not in stuffOnLandList):
                    print "Game over"
            if name == "bagOfGrains":
                if ("chicken" in stuffOnLandList) and ("man" not in stuffOnLandList):
                    print "Game over"
            if name == "man":
                if (("chicken" in stuffOnLandList) and
                   (("fox" in stuffOnLandList) or ("bagOfGrains" in stuffOnLandList))):
                    print "Game over"


    def getBoatPosition(self):
        return self.state.getBoatPosition()

    def getStuffInBoat(self):
        return self.state.getStuffInBoat()

    def getGameStatus(self):

        print "On the left side: " + ", ".join(self.state.getStuffOnLeftSide())
        print "On the right side: "
        print self.state.getStuffOnRightSide()
        print "Boat is at: "
        print self.state.getBoatPosition()
        print "Stuff in boat: "
        print self.state.getStuffInBoat()
