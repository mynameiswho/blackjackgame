import random

class BlackJackGame:
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

    def setup(self) -> None:
        '''Handles 1st phase of game. Deals 2 cards each to dealer and player, and modifies Ace values according to usual criteria. 
        '''        
        while len(self.player_cards) < 2:
            #Deal cards to player
            self._deal_to_player()
            
            #Handle if both cards are ace
            if len(self.player_cards) == 2:
                if self.player_cards[0].card_value == 11 and self.player_cards[1].card_value == 11:
                    self.player_cards[0].card_value = 1
                    self.player_score -= 10
        
        while len(self.dealer_cards) < 2:
            #Deal cards to dealer
            self._deal_to_dealer()

            #Handle if both cards are ace
            if len(self.dealer_cards) == 2:
                if self.dealer_cards[0].card_value == 11 and self.dealer_cards[1].card_value == 11:
                    self.dealer_cards[1].card_value = 1
                    self.dealer_score -= 10
    
    def hit(self) -> None:
        '''Use when player chooses to hit in 2nd phase of game. Deals 1 card to player, and modifies Ace values according to usual criteria.
        '''        
        #Player phase
        self._deal_to_player()

        #Handle if card is ace and player busts
        end_idx = len(self.player_cards) - 1
        if self.player_cards[end_idx].card_value == 11 and self.player_score > 21:
            self.player_cards[end_idx].card_value = 1
            self.player_score -= 10
    
    def stand(self) -> None:
        '''Use when player chooses to stand in 2nd phase of game. Deals cards to dealer until dealer_score >= 17.
        ''' 
        #Dealer phase
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
