import random

class BlackJackGame:
    def __init__(self, deck) -> None:

        self.deck = deck

        self.player_cards = []
        self.dealer_cards = []

        self.player_score = 0
        self.dealer_score = 0

    def setup(self) -> None:
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
        #Player phase
        self._deal_to_player()

        #Handle if card is ace and player busts
        end_idx = len(self.player_cards) - 1
        if self.player_cards[end_idx].card_value == 11 and self.player_score > 21:
            self.player_cards[end_idx].card_value = 1
            self.player_score -= 10
    
    def stand(self) -> None:
        #Dealer phase
        while self.dealer_score < 17:
            self._deal_to_dealer()

    def _deal_to_player(self) -> None:
        player_card = random.choice(self.deck)
        self.player_cards.append(player_card)
        self.deck.remove(player_card)
        self.player_score += player_card.card_value

    def _deal_to_dealer(self) -> None:
        dealer_card = random.choice(self.deck)
        self.dealer_cards.append(dealer_card)
        self.deck.remove(dealer_card)
        self.dealer_score += dealer_card.card_value
