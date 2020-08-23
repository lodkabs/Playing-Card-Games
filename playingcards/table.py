#table.py

import random
from word2number import w2n

suits = ("Spades", "Hearts", "Diamonds", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

symbols = {"Spades":"\u2660", "Hearts":"\u2665", "Diamonds":"\u2666", "Clubs":"\u2663"}
for r in ranks:
    try:
        symbols[r] = w2n.word_to_num(r)
    except:
        symbols[r] = list(r)[0]

# Create list containing deck
def shuffle_deck():
    '''
    Output: list containing all playing cards i.e. all rank/suit combinations
    '''
    global suits
    global ranks
    deck = []
    
    for s in suits:
        for r in ranks:
            deck.append((r, s))

    random.shuffle(deck)
    return deck

# Print hand
def print_hand(hand):
    '''
    Input: a list of lists, with a tuple [(rank, suit), faceup]
    Output: text-based image representation of hand
    '''
    card_lines = [""]*5
    for n in range(0,5):
        card_lines[n] = [""]*len(hand)

    for c, h in enumerate(hand):
        r = symbols[h[0][0]]
        s = symbols[h[0][1]]
        
        card_lines[0][c] = card_lines[4][c] = " ----- "
        if h[1]:
            card_lines[1][c] = "|" + str(r) + " "*((5-len(str(r)))) + "|"
            card_lines[2][c] = "|  " + s + "  |"
            card_lines[3][c] = "|" + " "*(5-len(str(r))) + str(r) + "|"
        else:
            card_lines[1][c] = card_lines[3][c] = "|     |"
            card_lines[1][c] = "|\u2554   \u2557|"
            card_lines[2][c] = "|  G  |"
            card_lines[3][c] = "|\u255a   \u255d|"
    
    result = ""
    for l in card_lines:
        result += "  ".join(l) + "\n"
    
    return result

# Defining player class
class Player():
    def __init__(self, name, dealer=False, money=100):
        self.name = name
        self.dealer = dealer
        self.money = money
        self.hand = []
    
    def add_card(self,card):
        self.hand.append(card)
        
    def empty_hand(self):
        self.hand = []
    
    def __str__(self):
        return f"{self.name}'s hand:\n" + print_hand(self.hand)

# Defining dealer class (subclass of player)
class Dealer(Player):
    def __init__(self, bank=0):
        self.bank = bank
        Player.__init__(self, name="Dealer", dealer=True, money=bank)

# Deal card from deck to player
def deal_card(deck, player, faceup, num=1):
    for n in range(0, num):
        player.add_card([deck.pop(), faceup])





