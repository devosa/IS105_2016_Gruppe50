''' Program for å komprimere tekstfiler.
    Programmet leser av en valgt tekst.txt fil og
    skriver en komprimert versjon av originalen '''

code4string = []

def code():


    tab1 = {}
    # Her genereres 256 text-elements
    for i in range(0, 256):
        tab1[1] = chr(i)
    return tab1

def encode(string, byte, tab):
    global code4string
    symbol = byte

    '''
    Sjekker om string og symbol allerede ligger i tabel. Om den er de så: string = string + symbol
    '''
    if (string + symbol) in tab.values():
        string = string + symbol
    else:
        for key,value in tab.iteritems():
            if value == string:
                code4string.append(key)

        # Setter en grense for hvor store tall som blir brukt og lengden.
        if (len(tab) >= 5):
            tab = code()

        # Legger string + symbol til table (tab)
        tab[max(tab.keys())+1] = string + symbol
        string = symbol

    return {'tab':tab, 'string':string}

# Åpner en fil som skal compress
def run(inFile, outFile):
    # Åpner inputfile
    f = open(inFile, 'r')
    # Åpner outputfile, 'write'
    outFile = open(outFile, 'w')
    temporary = {}
    # Legger til tekst-elementer til table(tab)
    tab = code()
    # String til å holde den aktuelle byte
    byte = ""
    # String til å holde den siste; Så den kan bli lagt til table(tab) senere.
    string = ""
    # Leser første byte
    byte = f.read(1)

    # Kaller global code4string
    global code4string

    # Kjør byten vi leste tidligere
    if (byte != ""):
        # Encoding første byte
        temporary = encode(string, byte, tab)
        # Legger til den returnerte verdien til strings.
        string = temporary['string']
        tab = temporary['tab']

    # Kjør: så lenge det er bytes i filen
    while (byte != ""):
        # Få byte
        byte = f.read(1)
        # Skriv til filen
        if (byte != ""):
            # Encode
            temporary = encode(string, byte, tab)
            # Legger til den returnerte verdien til variabler
            string = temporary['string']
            tab = temporary['tab']

    for key, value in tab.iteritems():
        if value == string:
            # Tilfører keyen til output table (tab)
            code4string.append(key)

    outFile.write(''.join(map(str,code4string)))

    toString = ''.join(map(str,code4string))
    return toString

# run('inFile.txt', 'output.txt') What file you want to encode, and the name of the file to be created
# Bare endre filnavnet og pass på at filen ligger lagret på samme sted som koden. Så kan du komprimere hva du vil
if __name__ == '__main__':
    run('hamlet.txt', 'output1.txt')
