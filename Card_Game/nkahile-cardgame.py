from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")


def clearDeck():
      for i in range(NUMCARDS):
        cardLoc[i]=0

      
def showDeck():
      print("Location of all cards")
      print('# 	 card 	 	 location')
      for i in range(NUMCARDS):
        name = playerName[cardLoc[i]]
        line = str(i) + " "+ translateIndexToName(i)+" " + name
        print(line)


def showHand(playerIndex):
      print ("Displaying "+ playerName[playerIndex] +" hand:")
      for i in range(NUMCARDS):
        if cardLoc[i] == playerIndex:
              print(translateIndexToName(i))
      
def assignCard(playerIndex):
      while(True):
        index = randint(0,51) 
        if cardLoc[index] == 0:
          cardLoc[index] = playerIndex
          return      

def translateIndexToName(i):
      suit = int(i/13)
      card = i%13
      name = rankName[card] +" of "+ suitName[suit]
      return name

def main():
      clearDeck() 

      for i in range(5):
        assignCard(PLAYER)
        assignCard(COMP)


      showDeck()
      showHand(PLAYER)
      showHand(COMP) 

main()