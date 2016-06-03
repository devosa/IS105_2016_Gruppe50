

import shelve, time, sys

class File(object):

    def __init__(self, name, type, parent=None, text=''): # Her sjekker den om noden er en fil. Om den er det så får vi Return True, hvis ikke, False.
        self.list = []
        self.name = name
        self.type = type
        self.time = time.asctime( time.localtime(time.time()) )
        self.parent = parent
        self.text = text

    def is_file(self, name):
        for node in self.list:
            if node.name == name:
                return True
        return False

    def is_dir(self, name): # Her sjekkes det om noden er i mappa. Returnerer true eller false etter som.
        if(self.is_file(name)) and self.get(name).type == 'dir':
            return True
        return False

    def get(self, name): # Her kan vi søke etter Filnavn og returnerer filnavn, hvis den eksisterer.
        for node in self.list:
            if node.name == name:
                return node

    def add(self, name, type, text=''): # Her legges det til fil, eventuelt innhold av filen, i en liste av filer.
        self.list.append(File(name, type, self, text))

    def remove(self, name): # Fjerner filen med innhold fra en liste av filer
        self.list.remove(self.get(name))

    def rename(self, name):  #Her kan vi endre navn på en fil eller en mappe
        self.name = name

    def copy(self, src, dest): # Kopiere filer til en annen plass.
        src = self.get(src)
        self.add(dest, src.type, src.text)

    def stat(self): # Skriver ut statistikk, oversikt.
        print 'Listing', self.name
        for node in self.list:
            print 'Name:', node.name, '; Created:', node.time, '; Type:', node.type

    def read(self): # Her leser vi innholdet i filen.
        print 'Reading file:', self.name
        print self.text

class FileSystem(object):

    COMMANDS = ['ls', 'mkdir', 'chdir', 'cd', 'rmdir', 'create', 'read', 'rm', 'mv', 'cp', 'help', 'exit']

    def __init__(self):
        self.io = shelve.open('file.sys', writeback=True)
        if self.io.has_key('fs'):
            self.root = self.io['fs']
        else:
            self.root = File('/', 'dir')
        self.curr = self.root

    def mkdir(self, cmd): # Funksjon for å lage directory(mappe). Hvis cmd er mellom 1 og 2 bir det utført.
        if len(cmd) < 2 or cmd[1] == '':
            print 'mkdir - make directory'
            print 'usage: mkdir <dir_name>'
        else:
            name = cmd[1]
            if self.curr.is_file(name) == False:
                self.curr.add(name, 'dir')
            else:
                print name, ' - already exists.';

    def chdir(self, cmd): #Funksjon for å skifte directory til gitt "bane"/spesifisert mappe.
        if len(cmd) < 2 or cmd[1] == '':
            print 'chdir - change directory.'
            print 'usage: chdir <dir_name>'
        else:
            name = cmd[1]
            if name == '..':
                if self.curr.parent is not None:
                    self.curr = self.curr.parent
            elif self.curr.is_dir(name):
                self.curr = self.curr.get(name)
            else:
                print name, ' - invalid directory.'

    def rmdir(self, cmd): #Funksjon for å slette mappe
        if len(cmd) < 2 or cmd[1] == '':
            print 'rmdir - remove directory'
            print 'usage: rmdir <dir_name>'
        else:
            name = cmd[1]
            if self.curr.is_dir(name):
                self.curr.remove(name)
                print 'Directory deleted.'
            else:
                print name, ' - invalid directory.'


    def rm(self, cmd): #Funksjon for å slette en fil, hvis cmd er mellom 1 og 2.
        if len(cmd) < 2 or cmd[1] == '':
            print 'rm - remove file'
            print 'usage: rm <file_name>'
        else:
            name = cmd[1]
            if self.curr.is_file(name) and not self.curr.is_dir(name):
                self.curr.remove(name)
                print 'File deleted.'
            else:
                print name, ' - invalid file.'

    def ls(self, cmd): # Lister ut innhold i mappen hvis cmd er over 1.
        if(len(cmd) > 1):
            print 'ls - list stats'
            print 'usage: ls'
        self.curr.stat()

    def create(self, cmd): #Funksjon for å lage en fil.
        if len(cmd) < 2 or cmd[1] == '':
            print 'create - create a file'
            print 'usage: create <file_name>'
        else:
            name = cmd[1]
            self.curr.add(name, 'file', raw_input('Enter file context: '))

    ''' Metode som foretar en sjekk for å se om cmd inneholder to eller flere tegn.
        Dersom dette stemmer, går filsystemet med på å lese filen som er spesifisert som parameter.
        Dersom dette ikke fungerer vil systemet nekte å kjøre filen, og man vi få opp feilmelding'''

    def read(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            print 'read - read a file'
            print 'usage: read <file_name>'
        else:
            name = cmd[1]
            if self.curr.is_file(name):
                self.curr.get(name).read()
            else:
                print name, 'invalid file'
''' Funksjon som brukes for å flytte en fil ved å gi den et nytt navn.
Den sjekker om paramteret cmd er tre eller flere tegn langt. Dersom dett er korrekt
vil programmet ta den gamle filen og gi den et nytt navn. '''

    def mv(self, cmd):
        if len(cmd) < 3 or cmd[1] == '':
            print 'mv - rename a file'
            print 'usage: mv <old_name> <new_name>'
        else:
            old_name = cmd[1]
            new_name = cmd[2]
            if self.curr.is_file(old_name):
                self.curr.get(old_name).rename(new_name)
            else:
                print old_name, 'invalid file'
''' Funksjon sjekker også validiteten til parameterene, og kopierer
deretter fra filen i src(source) og limer denne inn til dest (destination).
Dersom dette ikke stemmer vil det printes en feilmelding '''

    def cp(self, cmd):
        if len(cmd) < 3 or cmd[1] == '':
            print 'cp - copy a file'
            print 'usage: cp <src> <dest>'
        else:
            src = cmd[1]
            dest = cmd[2]
            if self.curr.is_file(src):
                self.curr.copy(src, dest)
            else:
                print src, 'invalid file'

    def save(self): # Lagre en fil.
        self.io['fs'] = self.root
        self.io.sync()

    def help(self, cmd): # Lister ut kommandoer som er tilgjengelige i systemet
        print 'COMMANDS: mkdir, ls, chdir, rmdir, create, read, mv, cp, rm, exit'

    def exit(self, cmd): # Avslutter
        sys.exit(0)

def main():
    fs = FileSystem()
    while True:
        cmd = raw_input('> ').split(' ');
        method = None
        try:
            method = getattr(fs, cmd[0])
        except AttributeError:
            print 'Invalid command. Type "help".'
        if method is not None and cmd[0] in FileSystem.COMMANDS and callable(method):
            method(cmd)
            fs.save()
        else:
            print 'Invalid command. Type "help".'
main()
