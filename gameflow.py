from cards import generate_card_deck
from cards import Card
from game import BlackJackGameMechanics
import tkinter as tk

'''This class will offer functions for:
    - Hit function: gamestate, return gamestate
    - Stand function: gamestate, return gamestate
    - Printing filled cards: frame to print in, cards to print
    - Printing empty cards: frame to print in, no of cards
    - Printing score: label to change, score
    - Generating filled card: private
    - Generating blank card: private'''

class BackOfficeFunctions:
    def __init__(self):
        pass

    def setup(self) -> BlackJackGameMechanics:
        deck = generate_card_deck()
        blackjackinstance = BlackJackGameMechanics(deck)
        blackjackinstance.first_deal()
        return blackjackinstance
    
    def print_stand_result(self, gamestate: BlackJackGameMechanics, lbl_to_change: tk.Label):
        dealer_score = gamestate.get_dealer_score()
        player_score = gamestate.get_player_score()
        if gamestate.dealer_bust():
            lbl_to_change['text'] = 'Dealer busts, Player wins!'
            return
        if dealer_score > player_score:
            lbl_to_change['text'] = 'Dealer beats Player!'
            return
        if player_score > dealer_score:
            lbl_to_change['text'] = 'Player beats Dealer!'
            return
        if player_score == dealer_score:
            lbl_to_change['text'] = 'Tie game!'
            return
    
    def destroy_widgets_in_frame(self, frame_to_use: tk.Frame) -> None:
        for widget in frame_to_use.winfo_children():
            widget.destroy()
    
    def first_phase_print_dealer(self, gamestate: BlackJackGameMechanics, frame_to_use: tk.Frame) -> None:
        first_card = gamestate.cards_dealer[0]
        self.print_filled_card(first_card, frame_to_use)
        self.print_blank_card(frame_to_use)
    
    def first_phase_print_player(self, gamestate: BlackJackGameMechanics, frame_to_use: tk.Frame, lbl_to_use: tk.Label) -> None:
        for card in gamestate.cards_player:
            self.print_filled_card(card, frame_to_use)
        lbl_to_use['text'] = f'Player score: {gamestate.get_player_score()}'

    def print_filled_card(self, card_to_print: Card, frame_to_use: tk.Frame) -> None:
        lbl = self._generate_filled_card(card_to_print, frame_to_use)
        lbl.pack(side=tk.LEFT, padx=10)

    def print_blank_card(self, frame_to_use: tk.Frame) -> None:
        lbl = self._generate_blank_card(frame_to_use)
        lbl.pack(side=tk.LEFT, padx=10)

    def _generate_filled_card(self, card: Card, frame_to_use: tk.Frame) -> tk.Label:
        suit = card.card_suit
        value = card.game_value
        card_to_print = tk.Label(
            master=frame_to_use,
            text=f'\n{suit}\n\n{value}\n',
            font=('Arial', 18),
            width=5,
            relief=tk.GROOVE,
            borderwidth=2
        )
        return card_to_print
    
    def _generate_blank_card(self, master_frame: tk.Frame) -> tk.Label:
        card_to_print = tk.Label(
            master=master_frame,
            text='\n\n\n\n',
            font=('Arial', 18),
            width=5,
            relief=tk.GROOVE,
            borderwidth=2
        )
        return card_to_print