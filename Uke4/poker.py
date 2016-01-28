'''Vi har laget en model for en kortstokk og utdeling av kort i python. Vi har en rekke for Suits, og en for ranks.
Så randomizer kortstokken en verdi fra hver rekke, og deler ut et ønsket antall kort til hver spiller.
I dette tilfellet har vi valgt to kort fordi vi vil ha et pokerspill. Så gjentas prosessen 5 ganger fordi vi er 5 spillere.
Vi har delt kortstokken i 2 rekker, en for suits og en for rank. Når du vet hvilken suit du har fått, så vet du også hvilken farge du har.
Det gjør at vi kun trenger 2 rekker og ikke 3.
Da blir også kortene delt opp i 4 kategorier, som gjør at vi kun trenger 14 ranks, isteden for 52 ranks. Dette forenkler prosessen, mer effektivt.'''

import random
import itertools

SUITS = ['-Klover', '-Ruter', '-Hjerter', '-Spar']
RANKS = ['2', '3', '4', '5','6', '7', '8', '9','10', 'J', 'Q', 'K', 'A']


DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
hand = random.sample(DECK, 5)

print hand

SUITS = ['-Klover', '-Ruter', '-Hjerter', '-Spar']
RANKS = ['2', '3', '4', '5','6', '7', '8', '9','10', 'J', 'Q', 'K', 'A']


DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
hand = random.sample(DECK, 5)

print hand

SUITS = ['-Klover', '-Ruter', '-Hjerter', '-Spar']
RANKS = ['2', '3', '4', '5','6', '7', '8', '9','10', 'J', 'Q', 'K', 'A']


DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
hand = random.sample(DECK, 5)

print hand

SUITS = ['-Klover', '-Ruter', '-Hjerter', '-Spar']
RANKS = ['2', '3', '4', '5','6', '7', '8', '9','10', 'J', 'Q', 'K', 'A']


DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
hand = random.sample(DECK, 5)

print hand

SUITS = ['-Klover', '-Ruter', '-Hjerter', '-Spar']
RANKS = ['2', '3', '4', '5','6', '7', '8', '9','10', 'J', 'Q', 'K', 'A']


DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
hand = random.sample(DECK, 5)

print hand
