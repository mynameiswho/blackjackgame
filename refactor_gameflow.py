from cards import generate_card_deck
from cards import Card
from game import BlackJackGameMechanics
import tkinter as tk
from refactor_app import ApplicationWindow

class DynamicVisuals:
    def __init__(self, window: ApplicationWindow):
        deck = generate_card_deck()
        self.gamestate = BlackJackGameMechanics(deck)
        self.gui = window
        self.gui.gui_setup(self.hit, self.stand)
        self.gamestate.run_first_phase()
    
    def hit(self):
        print('hey')
    
    def stand(self):
        print('yo')

    def print_dealer_cards(self, cards_to_print: list) -> None:
        for card in cards_to_print:
            lbl = self._generate_filled_card(card, self.gui.frm_dealer)
            lbl.pack(side=tk.LEFT, padx=10)

    def print_player_cards(self, cards_to_print: list) -> None:
        for card in cards_to_print:
            lbl = self._generate_filled_card(card, self.gui.frm_player)
            lbl.pack(side=tk.LEFT, padx=10)
    
    def _print_dealer_score(self, lbl_to_change: tk.Label) -> None:
        lbl_to_change['text'] = f'Dealer score: {self.gamestate.get_dealer_score()}'

    def _print_player_score(self, lbl_to_change: tk.Label) -> None:
        lbl_to_change['text'] = f'Player score: {self.gamestate.get_player_score()}'

    def _generate_filled_card(card_data: Card, master_frame: tk.Frame) -> tk.Label:
        suit = card_data.card_suit
        value = card_data.game_value
        card_to_print = tk.Label(
            master=master_frame,
            text=f'\n{suit}\n\n{value}\n',
            font=('Arial', 18),
            width=5,
            relief=tk.GROOVE,
            borderwidth=2
        )
        return card_to_print
    
    def _generate_blank_card(master_frame: tk.Frame) -> tk.Label:
        card_to_print = tk.Label(
            master=master_frame,
            text='\n\n\n\n',
            font=('Arial', 18),
            width=5,
            relief=tk.GROOVE,
            borderwidth=2
        )
        return card_to_print
    
if __name__ == '__main__':
    r = tk.Tk()
    w = ApplicationWindow(r)
    dv = DynamicVisuals(w)