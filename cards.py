
class Card:
    def __init__(self, card_suit, deck_value, game_value) -> None:
        #Suit of card
        self.card_suit = card_suit
        #Representing value of card (Ace / King / Queen etc)
        self.deck_value = deck_value
        #Nominal value in game (11/1 for Ace / 10 for King etc)
        self.game_value = game_value

def generate_card_deck() -> None:
    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    # The suit value 
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
    # The type of card
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    # The card value
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    deck = []

    for suit in suits:
        for cardnumber in cards:
            deck.append(Card(suits_values[suit], cardnumber, cards_values[cardnumber]))
    
    return deck