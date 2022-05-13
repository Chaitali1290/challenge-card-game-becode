 
import black
from card import Card
import random

#creating a class player

class Player:

    cards=[]
    turn_count=0
    number_of_cards=0
    history=[]

    def __init__(self,cards,turn_count,number_of_cards,history):
        self.cards=cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history=history

    def play(self):
        random_card = random.choice(Card)  #randomly pick the card
        self.history.append(random_card) #add a card in players history
        return Card

from random import shuffle

class Deck(Card):
    def __init__(self):
        self.colors =["black","red"]
        self.icons = ['♥','♦','♣','♠']
        self.values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = []

    def fill_deck(self): #method to crete a deck of 52 cards
        for each_color in self.colors:
            if each_color == "black":
                for each_icon in self.icons:
                    if each_icon == "♠" or each_icon == "♣":
                        for each_value in self.values:
                            d=Card(each_color,each_icon,each_value)
                            self.cards.append(d)
            else:
                for each_icon in self.icons:
                    if each_icon == "♥" or each_icon == "♦":
                        for each_value in self.values:
                            d=Card(each_color,each_icon,each_value)
                            self.cards.append(d)
                            #print("{} {} of {}".format(each_color,each_icon,each_value))

    def shuffle(self):
        shuffle(self.cards)

    def distribute(self,list_of_players):
        while len(self.cards) > 0:
            for each_player in list_of_players:
                if len(self.cards) > 0:
                    card=self.cards[0]
                    each_player.cards.append(card)
                    self.cards=self.cards.remove(0)

deck=Deck()
deck1=deck.fill_deck()
print(deck1)

card=deck.cards
print(card)
print(len(card))



                
            