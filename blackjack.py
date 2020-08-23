'''
A rudementary blackjack game
'''

from word2number import w2n
from playingcards import table

values = {}
for r in table.ranks:
    try:
        values[r] = w2n.word_to_num(r)
    except:
        if r == "Ace":
            values[r] = 11
        else:
            values[r] = 10

def hand_value(hand):
    v = 0
    aces = 0
    for card in hand:
        v += values[card[0][0]]
        if card[0][0] == "Ace":
            aces += 1
    
    if v > 21 and aces > 0:
        for a in range(0,aces):
            v -= 10
            if v <= 21:
                break

    return v

# Intro
for s, w in zip(list(table.suits), ["Let's", "Play", "Some", "Blackjack!"]):
    print(f"{table.symbols[s]} {w}")
print("\n")

dealer = table.Dealer()
player1 = table.Player(name="Player 1")

deck = table.shuffle_deck()

def bet(player):
    print(f"\n{player.name}'s current amount: {player.money}")
    while True:
        try:
            bid = int(input(f"How much would {player.name} like to bet?: "))
        except:
            print("Please enter a valid amount.\n")
            continue
        else:
            if bid > player.money:
                print("Betting more than available amount.\n")
                continue
            else:
                return bid

def print_table():
    print("\n")
    print(dealer)
    print(player1)
    print(f"{player1.name} value: {hand_value(player1.hand)}\n")

def next_round():
    dealer.empty_hand()
    player1.empty_hand()
    
    table.deal_card(deck, dealer, True)
    table.deal_card(deck, dealer, False)
    table.deal_card(deck, player1, True, 2)

game_on = True

while(game_on):
    player1_bet = bet(player1)
    next_round()
    
    win = False
    while True:
        print_table()
        player1_value = hand_value(player1.hand)
        
        if player1_value > 21:
            print("Bust!")
            break
        elif player1_value == 21:
            print("Blackjack!")
            win = True
            break
        else:
            hit = False
            while True:
                hit = input(f"Would {player1.name} like to hit? (y/n): ")
                if hit.lower() == "y" or hit.lower() == "n":
                    break
                else:
                    print("Please enter a valid input (y/n).\n")
                    continue
            
            if hit.lower() == "y":
                table.deal_card(deck, player1, True)
                continue
            else:
                for f, card in enumerate(dealer.hand):
                    dealer.hand[f][1] = True
                
                dealer_value = hand_value(dealer.hand)
                while(dealer_value < player1_value and dealer_value < 17):
                    table.deal_card(deck, dealer, True)
                    dealer_value = hand_value(dealer.hand)
                    
                print_table()
                print(f"{dealer.name} value: {hand_value(dealer.hand)}\n")
                if dealer_value > 21:
                    print(f"{dealer.name} bust!")
                    win = True
                    break
                elif dealer_value < player1_value:
                    print(f"{player1.name} wins!")
                    win = True
                    break
                else:
                    print(f"{dealer.name} wins!")
                    break
        break
    
    if win:
        player1.money += player1_bet
        dealer.money -= player1_bet
    else:
        player1.money -= player1_bet
        dealer.money += player1_bet
    
    if player1.money == 0:
        print(f"{player1.name} is out to money.\n{player1.name} whited out!")
        game_on = False
    else:
        while True:
            again = input("Another round? (y/n): ")

            if again.lower() != "y" and again.lower() != "n":
                print("Please enter a valid input (y/n).\n")
                continue
            break
                
        if again.lower() != "y":
            game_on = False
        else:
            if len(deck) < 10:
                print("Shuffling deck...")
                deck = table.shuffle_deck()







