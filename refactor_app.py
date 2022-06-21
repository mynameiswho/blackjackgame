import tkinter as tk
from game import BlackJackGameMechanics
from cards import generate_card_deck

class ApplicationWindow(tk.Frame):
    def __init__(self, parent: tk.Tk, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        #self.gamestate = self.game_setup()
        self.gui_setup()

    def game_setup(self) -> BlackJackGameMechanics:
        deck = generate_card_deck()
        gamestate = BlackJackGameMechanics(deck)
        gamestate.run_first_phase()
        return gamestate
    
    def gui_setup(self):
        self.configure_parent()
        self.create_and_configure_frms()
        self.create_and_configure_lbls()
        self.create_and_configure_btns()

    def configure_parent(self):
        self.parent.title('Simple BlackJack Game')
        self.parent.rowconfigure([0,1], minsize=200, weight=1)
        self.parent.rowconfigure([2, 3], minsize=50)
        self.parent.columnconfigure(0, minsize=75)
        self.parent.columnconfigure(1, minsize=500, weight=1)
            
    def create_and_configure_frms(self):
        self.frm_dealer = tk.Frame(master=self.parent, relief=tk.SUNKEN, borderwidth=3, background='white')
        self.frm_player = tk.Frame(master=self.parent, relief=tk.SUNKEN, borderwidth=3, background='white')
        self.frm_btns = tk.Frame(master=self.parent)
        self.frm_dealer.grid(row=0, column=1, sticky='nsew')
        self.frm_player.grid(row=1, column=1, sticky='nsew')
        self.frm_btns.rowconfigure(0, weight=1)
        self.frm_btns.columnconfigure([0, 1], weight=1)
        self.frm_btns.grid(row=3, column=1, sticky='nsew')
    
    def create_and_configure_lbls(self):
        lbl_dealer = tk.Label(master=self.parent, text='DEALER')
        lbl_dealer_score = tk.Label(master=self.parent, text= 'Dealer score: ')
        lbl_player = tk.Label(master=self.parent, text='PLAYER')
        lbl_player_score = tk.Label(master=self.parent, text= 'Player score: ')
        lbl_status = tk.Label(master=self.parent, text='Make your choice by either Hitting or Standing!')
        lbl_dealer.grid(row=0, sticky='ew')
        lbl_dealer_score.grid(row=0, sticky='s', padx=10, pady=10)
        lbl_player.grid(row=1, sticky='ew')
        lbl_player_score.grid(row=1, sticky='s', padx=10, pady=10)
        lbl_status.grid(row=2, column=1, sticky='nsew')
    
    def create_and_configure_btns(self):
        btn_hit = tk.Button(master=self.frm_btns, text='Hit', command= lambda: self.hit(self.gamestate))
        btn_stand = tk.Button(master=self.frm_btns, text='Stand', command= lambda: self.stand(self.gamestate))    
        btn_hit.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        btn_stand.grid(row=0, column=1, sticky='ew', padx=5, pady=5)
    
    def hit(self, gamestate: BlackJackGameMechanics):
        pass

    def stand(self, gamestate: BlackJackGameMechanics):
        pass

#Suggested to create one class per major part of GUI: eg. Statusbar, Toolbar, Navbar

if __name__ == "__main__":
    root = tk.Tk()
    ApplicationWindow(root).grid(sticky="nsew")
    root.mainloop()