import tkinter as tk
from game import BlackJackGameMechanics
from cards import Card, generate_card_deck

class MainApplication(tk.Frame):
    def __init__(self, parent: tk.Tk, gamestate: BlackJackGameMechanics, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gamestate = gamestate
        self.set_up_gui()
    
    def set_up_gui(self):
        #Set up parent dimensions
        self.parent.title('Simple BlackJack Game')
        self.parent.rowconfigure([0,1], minsize=200)
        self.parent.rowconfigure([2, 3], minsize=50)
        self.parent.columnconfigure(0, minsize=75)
        self.parent.columnconfigure(1, minsize=500)

        #Frames
        frm_dealer = tk.Frame(master=self.parent, relief=tk.SUNKEN, borderwidth=3, background='white')
        frm_player = tk.Frame(master=self.parent, relief=tk.SUNKEN, borderwidth=3, background='white')
        frm_status = tk.Frame(master=self.parent, background='white')
        frm_btns = tk.Frame(master=self.parent)

        #Labels
        lbl_dealer = tk.Label(master=self.parent, text='DEALER')
        lbl_dealer_score = tk.Label(master=self.parent, text= 'Dealer score: ')
        lbl_player = tk.Label(master=self.parent, text='PLAYER')
        lbl_player_score = tk.Label(master=self.parent, text= 'Player score: ')
        lbl_status = tk.Label(master=frm_status, text='Make your choice by either Hitting or Standing!')

        #Buttons
        btn_hit = tk.Button(master=frm_btns, text='Hit', command= lambda: self.hit(self.gamestate))
        btn_stand = tk.Button(master=frm_btns, text='Stand', command= lambda: self.stand(self.gamestate))

        #Layout frames
        frm_dealer.grid(row=0, column=1, sticky='nsew')
        frm_player.grid(row=1, column=1, sticky='nsew')

        frm_status.rowconfigure(0, weight=1)
        frm_status.columnconfigure(0, weight=1)
        frm_status.grid(row=2, column=1, sticky='nsew')

        frm_btns.rowconfigure(0, weight=1)
        frm_btns.columnconfigure([0, 1], weight=1)
        frm_btns.grid(row=3, column=1, sticky='nsew')

        #Layout labels
        lbl_status.grid(sticky='nsew')
        lbl_dealer.grid(row=0, sticky='ew')
        lbl_dealer_score.grid(row=0, sticky='s', padx=10, pady=10)
        lbl_player.grid(row=1, sticky='ew')
        lbl_player_score.grid(row=1, sticky='s', padx=10, pady=10)

        #Layout buttons
        btn_hit.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        btn_stand.grid(row=0, column=1, sticky='ew', padx=5, pady=5)
    
    def hit(self, gamestate: BlackJackGameMechanics):
        pass

    def stand(self, gamestate: BlackJackGameMechanics):
        pass
                

#Suggested to create one class per major part of GUI: eg. Statusbar, Toolbar, Navbar

if __name__ == "__main__":
    deck = generate_card_deck()
    gamestate = BlackJackGameMechanics(deck)
    
    root = tk.Tk()
    MainApplication(root, gamestate).pack(side="top", fill="both", expand=True)
    root.mainloop()