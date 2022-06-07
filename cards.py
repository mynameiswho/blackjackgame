
class Card:
    '''Object identifying specificities of a playing card.
    
    Attributes:
        suit -- the suit in UNICODE format
        value -- the card value, e.g. 10, J, Q etc
        card_value -- nominal card value in BlackJack game, e.g. 11 / 1 for Ace, 10 for King etc
    '''
    def __init__(self, suit: str, value: str, card_value: int) -> None:        
        '''Arguments:
            suit -- the suit of the card
            value -- the card value, e.g. A, K, 10
            card_value -- the nominal card value in BlackJack game, e.g. A = 11, K = 10
        '''        
        #Suit of card
        self.suit = suit
        #Representing value of card (Ace / King / Queen etc)
        self.value = value
        #Nominal value in game (11/1 for Ace / 10 for King etc)
        self.card_value = card_value

def generate_card_deck() -> list:
    '''Generates 1 deck of 52 playing cards based on the Card class.

    Returns:
        list with deck of all 52 playing cards.
    '''    
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    deck = []
    for suit in suits:
        for cardnumber in cards:
            deck.append(Card(suits_values[suit], cardnumber, cards_values[cardnumber]))
    
    return deck