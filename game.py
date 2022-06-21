import random
from cards import Card

class BlackJackGameMechanics:
    '''Object representing a BlackJack game with functions for each phase. Excluding logic for wins / busts.
    
    Attributes:
        deck -- the deck currently being used, excludes cards already dealt
        cards_player -- cards dealt to player
        cards_dealer -- cards dealt to dealer
        score_player -- score of player
        score_dealer -- score of dealer
    '''
    def __init__(self, deck: list) -> None:     
        self.deck = deck
        self.cards_player = []
        self.cards_dealer = []
        self.score_player = 0
        self.score_dealer = 0

    def run_first_phase(self) -> None:
        '''Handles 1st phase of game. Deals 2 cards each to dealer and player, and modifies Ace values according to usual criteria. 
        '''        
        while len(self.cards_player) < 2:
            self._deal_to_player()
        if self._check_if_two_aces(self.cards_player):
            self._reduce_ace_value(self.cards_player[0], self.score_player)

        while len(self.cards_dealer) < 2:
            self._deal_to_dealer()
        if self._check_if_two_aces(self.cards_dealer):
            self._reduce_ace_value(self.cards_dealer[1], self.score_dealer)

    def hit(self) -> None:
        '''Used when player chooses to hit in 2nd phase of game. Deals 1 card to player, and modifies Ace values according to usual criteria.
        '''        
        self._deal_to_player()
        last_card_idx = len(self.cards_player) - 1
        if self._check_if_ace_and_bust(self.cards_player[last_card_idx], self.score_player):
            self._reduce_ace_value(self.cards_player[last_card_idx], self.score_player)
    
    def stand(self) -> None:
        '''Used when player chooses to stand in 2nd phase of game. Deals cards to dealer until dealer_score >= 17.
        ''' 
        while self.score_dealer < 17:
            self._deal_to_dealer()

    def _deal_to_player(self) -> None:
        '''Used only by setup(), hit() and / or stand()
        '''              
        player_card = random.choice(self.deck)
        self.cards_player.append(player_card)
        self.deck.remove(player_card)
        self.score_player += player_card.game_value

    def _deal_to_dealer(self) -> None:
        '''Used only by setup(), hit() and / or stand()
        '''
        dealer_card = random.choice(self.deck)
        self.cards_dealer.append(dealer_card)
        self.deck.remove(dealer_card)
        self.score_dealer += dealer_card.game_value
    
    def _check_if_two_aces(self, dealt_cards: list) -> bool:
        '''Used only by setup()
        '''
        first = dealt_cards[0]
        second = dealt_cards[1]
        ace_value = 11
        if first.game_value == ace_value and second.game_value == ace_value:
            return True
        else:
            return False
    
    def _check_if_ace_and_bust(self, card_to_check: Card, score_tracker: int):
        '''Used only by hit()
        '''
        ace_value = 11
        if card_to_check.game_value == ace_value and score_tracker > 21:
            return True
        else:
            return False
    
    def _reduce_ace_value(self, ace_to_adjust: Card, score_tracker: int) -> None:
        '''Used by setup() / hit()
        '''
        ace_to_adjust.game_value = 1
        score_tracker -= 10