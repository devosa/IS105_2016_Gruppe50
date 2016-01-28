def printBinaryForText(text):
    binary = ""

    for i in range(0,len(text)):
        number = ord(text[i])
        binary += format(number, "08b")

    print(binary)


printBinaryForText("hei")
printBinaryForText("du")
printBinaryForText("der")
