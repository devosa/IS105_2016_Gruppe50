'''
    UDP socket tjener.

    En enkel server som kan motta meldinger fra en klient.
    Programmet lar brukeren sende meldinger til en server hvor serveren responderer.


    Programmet har kommunikasjonen som trengs mellom klient/tjener for å potensielt kunne endre tilstand hos en tjener
    som ville ha kjørt elvekryssningsspillet. Det er dog ikke implementert grunnet;
    1. Mangel på kunnskap.

    Vi har likevel lært hvor "enkelt" det kan være å sette opp en klient/tjener for å kunne kommunisere på et nettverk,
    noe som var svært lærerikt.

    





'''

import socket #bruker modulen socket som er den del av standard biblioteket til python.
import sys #for å kunne avslutte programmet.

HOST = ''
PORT = 8888 # ved å holde seg over port 1024 unngår man at man bruker en port som er priviligert til noe annet. f.eks port 80 som er for http.



#Lager et socket av protokolltypen UDP.
#Ved å spesifisere socket.SOCK_DGRAM benytter man UDP protokollen. For TCP-connection ville man ha brukt, socket.SOCK_STREAM


try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

# Binder socket til 'localhost' (pcen som kjører server.py) og porten 8888.

try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'



'''
    Her måtte man ha implementert en måte slik at klienten fikk tilbake en respons på at tilstanden
    hadde endret seg i elvekrysningsspillet og ikke bare at klienten får tilbake samme melding som den sendte.
'''

while 1:
    #Snakker med klienten.
    d = s.recvfrom(1024) #spesifiserer hvor stor bufferen skal være. Hvor mye data skal man laste til enhver tid.
    data = d[0]
    addr = d[1]

    if not data:
        break

    reply = 'OK...' + data

    s.sendto(reply , addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()

s.close()
