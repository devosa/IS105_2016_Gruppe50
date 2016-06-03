''' Spillet ble i første omgang laget for å kunne kjøre på et GUI.
    Det er derfor ikke implementert funksjoner som kan ta input fra brukeren
    for å kunne endre tilstanden i spillet.

    Det er kun opprettet et testklasse for å se at logikken i spillet fungerer
    som den skal. Her ville man bare ha laget funksjoner som kunne ta input fra
    brukeren (r_rawinput) som igjen kalte på de eksisterende metodene, men dette
    ble ikke implementert grunnet dårlig tid, og større ønske om å få til GUI.

    For å se at logikken i spillet fungerer som den skal kjører man test.py
    '''

from game import RiverGame

game = RiverGame()

game.play()

game.putInBoat("chicken")
game.putInBoat("man")

game.moveBoat()

game.putOnLand("chicken")

game.moveBoat()

game.putInBoat("bagOfGrains")

game.moveBoat()

game.putOnLand("man")
game.putOnLand("bagOfGrains")
game.putInBoat("chicken")
game.putInBoat("man")

game.moveBoat()


game.putOnLand("man")
game.putOnLand("chicken")
game.putInBoat("fox")
game.putInBoat("man")

game.moveBoat()

game.putOnLand("fox")

game.moveBoat()

game.putInBoat("chicken")

game.moveBoat()

game.putOnLand("man")

game.putOnLand("chicken")

game.getGameStatus()
