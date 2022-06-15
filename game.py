import random
from cards import Card

class BlackJackGameMechanics:
    '''Object representing a BlackJack game with functions for each phase. Excluding logic for wins / busts.
    
    Attributes:
        deck -- the deck currently being used, excluding cards already dealt
        player_cards -- cards dealt to player
        dealer_cards -- cards dealt to dealer
        player_score -- score of player
        dealer_score -- score of dealer
    '''

    def __init__(self, deck) -> None:     
        self.deck = deck

        self.player_cards = []
        self.dealer_cards = []

        self.player_score = 0
        self.dealer_score = 0

    def run_first_phase(self) -> None:
        '''Handles 1st phase of game. Deals 2 cards each to dealer and player, and modifies Ace values according to usual criteria. 
        '''        
        while len(self.player_cards) < 2:
            #Deal cards to player
            self._deal_to_player()
            
        #Handle if both player cards are ace
        if self._check_if_two_aces(self.player_cards):
            self._reduce_ace_value(self.player_cards[0], self.player_score)

        while len(self.dealer_cards) < 2:
            #Deal cards to dealer
            self._deal_to_dealer()

        #Handle if both dealer cards are ace
        if self._check_if_two_aces(self.dealer_cards):
            self._reduce_ace_value(self.dealer_cards[1], self.dealer_score)

    def hit(self) -> None:
        '''Use when player chooses to hit in 2nd phase of game. Deals 1 card to player, and modifies Ace values according to usual criteria.
        '''        
        #Player phase
        self._deal_to_player()

        #Handle if card is ace and player busts
        last_card_idx = len(self.player_cards) - 1
        if self._check_if_ace_and_bust(self.player_cards[last_card_idx], self.player_score):
            self._reduce_ace_value(self.player_cards[last_card_idx], self.player_score)
    
    def stand(self) -> None:
        '''Use when player chooses to stand in 2nd phase of game. Deals cards to dealer until dealer_score >= 17.
        ''' 
        while self.dealer_score < 17:
            self._deal_to_dealer()

    def _deal_to_player(self) -> None:
        '''Private. Used only by setup(), hit() and / or stand()
        '''              
        player_card = random.choice(self.deck)
        self.player_cards.append(player_card)
        self.deck.remove(player_card)
        self.player_score += player_card.card_value

    def _deal_to_dealer(self) -> None:
        '''Private. Used only by setup(), hit() and / or stand()
        '''
        dealer_card = random.choice(self.deck)
        self.dealer_cards.append(dealer_card)
        self.deck.remove(dealer_card)
        self.dealer_score += dealer_card.card_value
    
    def _check_if_two_aces(self, dealt_cards: list) -> bool:
        '''Private. Used only by setup()
        '''
        first = dealt_cards[0]
        second = dealt_cards[1]
        ace_value = 11
        
        if first.card_value == ace_value and second.card_value == ace_value:
            return True
        else:
            return False
    
    def _check_if_ace_and_bust(self, card_to_check: Card, score_tracker: int):
        
        ace_value = 11

        if card_to_check.card_value == ace_value and score_tracker > 21:
            return True
        else
            return False
    
    def _reduce_ace_value(self, ace_to_adjust: Card, score_tracker: int) -> None:
        '''Private. Used only by setup() / hit()
        '''
        ace_to_adjust.card_value = 1
        score_tracker -= 10