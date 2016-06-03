# coding=utf-8

''' Kode for å lage lærret, objekter og kunne flytte på de ved å binde
    de til forskjellige knapper.

    Det ble ikke tid til å implementere et vindu for å vise "game over/ Du har vunnet".
    Dette hadde vært en smal sak, men det ble rett og slett ikke tid.

    For å se tilstanden til verdenen anbefales det at man har oppe terminal vinduet
    menst man spiller spillet.

'''

from Tkinter import *
from game import RiverGame

game = RiverGame()

root = Tk()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack()

def putInBoat(type):
    def callback():
        side = game.getBoatPosition()
        if type == "chicken":
            game.putInBoat("chicken")
            # første kallet e venstre land. andre e høyre land. gjelder alle nedover. juster posisjonen(x,y)
            canvas.move(chicken, 300, -30) if side == "left" else canvas.move(chicken, -150, -30)
        elif type == "fox":
            game.putInBoat("fox")
            canvas.move(wolf, 200, -30) if side == "left" else canvas.move(wolf, -250, -30)
        elif type == "man":
            game.putInBoat("man")
            canvas.move(man, 250, -30) if side == "left" else canvas.move(man, -200, -30)
        elif type == "bagOfGrains":
            game.putInBoat("bagOfGrains")
            canvas.move(bagOfCorn, 250, -28) if side == "left" else canvas.move(bagOfCorn, -200, -28)

    return callback


def putOnLand(type):

    def callback():
        side = game.getBoatPosition()
        if type == "chicken":
            game.putOnLand("chicken")
            # første kallet e venstre land. andre e høyre land. gjelder alle nedover. juster posisjonen(x,y)
            canvas.move(chicken, -300, 30) if side == "left" else canvas.move(chicken, 150, 30)
        elif type == "fox":
            game.putOnLand("fox")
            canvas.move(wolf, -200, 30) if side == "left" else canvas.move(wolf, 250, 30)
        elif type == "man":
            game.putOnLand("man")
            canvas.move(man, -250, 30) if side == "left" else canvas.move(man, 200, 30)
        elif type == "bagOfGrains":
            game.putOnLand("bagOfGrains")
            canvas.move(bagOfCorn, -250, 28) if side == "left" else canvas.move(bagOfCorn, 200, 28)

    return callback

def moveBoat():
    side = game.getBoatPosition()
    stuffInBoat = game.getStuffInBoat()

    if "chicken" in stuffInBoat:
          canvas.move(chicken, 330, 0) if side == "left" else canvas.move(chicken, -330, 0)
    if "fox" in stuffInBoat:
          canvas.move(wolf, 330, 0) if side == "left" else canvas.move(wolf, -330, 0)
    if "man" in stuffInBoat:
          canvas.move(man, 330, 0) if side == "left" else canvas.move(man, -330, 0)
    if "bagOfGrains" in stuffInBoat:
          canvas.move(bagOfCorn, 330, 0) if side == "left" else canvas.move(bagOfCorn, -330, 0)

    game.moveBoat()
    canvas.move(boat, 330, 0) if side == "left" else canvas.move(boat, -330, 0)

    #return callback


button1 = Button(bottomFrame, text="Sett mann i båt", fg="blue", command=putInBoat("man"))
button2 = Button(bottomFrame, text="Sett kylling i båt", fg="yellow", command=putInBoat("chicken"))
button3 = Button(bottomFrame, text="Sett korn i båt", fg="purple", command=putInBoat("bagOfGrains"))
button4 = Button(bottomFrame, text="Sett rev i båt", fg="red", command=putInBoat("fox"))
button5 = Button(bottomFrame, text="Kryss elven", fg="brown", command=moveBoat)
button6 = Button(bottomFrame, text="Sett mann utav båt", fg="blue", command=putOnLand("man"))
button7 = Button(bottomFrame, text="Sett kylling ut av båt", fg="yellow", command=putOnLand("chicken"))
button8 = Button(bottomFrame, text="Sett korn ut av båt", fg="purple", command=putOnLand("bagOfGrains"))
button9 = Button(bottomFrame, text="Sett sett rev utav båt", fg="red", command=putOnLand("fox"))

#button10 = Button(bottomFrame, text="Kryss elven", fg="brown")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=RIGHT)
button7.pack(side=RIGHT)
button8.pack(side=RIGHT)
button9.pack(side=RIGHT)


canvas = Canvas(topFrame, width=1440, height=500)
canvas.pack()

label = Label(root, text="Rivercrossing game!")
label.pack()

chicken = canvas.create_oval(250, 450, 290, 480, fill="yellow")
wolf = canvas.create_rectangle(300, 450, 340, 480, fill="red")
man = canvas.create_rectangle(350, 420, 380, 480, fill="blue")
bagOfCorn = canvas.create_arc(200, 465, 240, 490, fill="purple")
boat = canvas.create_rectangle(450, 480, 650, 450, fill="black")

sandBankLeft = canvas.create_rectangle(0, 480, 450, 520, fill="brown")
sandBankRight = canvas.create_rectangle(980, 480, 1440, 520, fill="brown")
water = canvas.create_rectangle(450, 520, 980, 480, fill="blue")
sun = canvas.create_oval(700, 50, 600, 150, fill="yellow")


root.mainloop()
