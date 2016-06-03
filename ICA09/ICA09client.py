'''
    UDP socket klient
'''

import socket   #bruker modulen socket som er den del av standard biblioteket til python.
import sys  #for å kunne avslutte programmet.

#Lager et socket av protokolltypen UDP.
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

host = '192.168.11.213' # IP-adressen/domenenavn til maskinen som fungerer som tjener. Lokal IP-adresse i dette tilfellet.
port = 8888; # ved å holde seg over port 1024 unngår man at man bruker en port som allerede er i bruk. f.eks port 80 som er for http

while(1) :
    msg = raw_input('Enter message to send : ')

    try :
        s.sendto(msg, (host, port))

        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print 'Server reply : ' + reply

    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
