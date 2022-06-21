from cards import generate_card_deck
from game import BlackJackGameMechanics

class GameActions:
    def __init__(self):
        d = generate_card_deck()
        self.gamestate = BlackJackGameMechanics(d)
        self.gamestate.run_first_phase()
    
    def p(self):
        pass

#Suggested to create one class per major part of GUI: eg. Statusbar, Toolbar, Navbar