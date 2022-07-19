import tkinter as tk
from gameflow import BackOfficeFunctions

class ApplicationWindow(tk.Frame):
    def __init__(self, parent: tk.Tk, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.bofunctions = BackOfficeFunctions()
        self.gamestate = self.bofunctions.setup()
        self.gui_setup()
        self.game_setup()
    
    def gui_setup(self):
        self.parent_config()
        self.frms_create_and_config()
        self.lbls_create_and_config()
        self.btns_create_and_config()
    
    def game_setup(self):
        for frm in [self.frm_dealer, self.frm_player]:
            self.bofunctions.destroy_widgets_in_frame(frm)
        self.bofunctions.first_phase_print_dealer(self.gamestate, self.frm_dealer)
        self.bofunctions.first_phase_print_player(self.gamestate, self.frm_player, self.lbl_player_score)
        self.first_phase_check_blackjack()

    def parent_config(self):
        self.parent.title('Simple BlackJack Game')
        self.parent.rowconfigure([0,1], minsize=200, weight=1)
        self.parent.rowconfigure([2, 3], minsize=50)
        self.parent.columnconfigure(0, minsize=75)
        self.parent.columnconfigure(1, minsize=500, weight=1)
            
    def frms_create_and_config(self):
        self.frm_dealer = tk.Frame(master=self.parent, relief=tk.SUNKEN, borderwidth=3, background='white')
        self.frm_player = tk.Frame(master=self.parent, relief=tk.SUNKEN, borderwidth=3, background='white')
        self.frm_btns = tk.Frame(master=self.parent)
        self.frm_dealer.grid(row=0, column=1, sticky='nsew')
        self.frm_player.grid(row=1, column=1, sticky='nsew')
        self.frm_btns.rowconfigure(0, weight=1)
        self.frm_btns.columnconfigure([0, 1], weight=1)
        self.frm_btns.grid(row=3, column=1, sticky='nsew')
    
    def lbls_create_and_config(self):
        self.lbl_dealer = tk.Label(master=self.parent, text='DEALER')
        self.lbl_dealer_score = tk.Label(master=self.parent, text= '')
        self.lbl_player = tk.Label(master=self.parent, text='PLAYER')
        self.lbl_player_score = tk.Label(master=self.parent, text= '')
        self.lbl_status = tk.Label(master=self.parent, text='Make your choice by either Hitting or Standing!')
        self.lbl_dealer.grid(row=0, sticky='ew')
        self.lbl_dealer_score.grid(row=0, sticky='s', padx=10, pady=10)
        self.lbl_player.grid(row=1, sticky='ew')
        self.lbl_player_score.grid(row=1, sticky='s', padx=10, pady=10)
        self.lbl_status.grid(row=2, column=1, sticky='nsew')
    
    def btns_create_and_config(self):
        tk.Button(master=self.frm_btns, text='Hit', command=self.hit).grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        tk.Button(master=self.frm_btns, text='Stand', command=self.stand).grid(row=0, column=1, sticky='ew', padx=5, pady=5)
    
    def hit(self):
        self.bofunctions.destroy_widgets_in_frame(self.frm_player)
        self.gamestate.hit()
        for card in self.gamestate.cards_player:
            self.bofunctions.print_filled_card(card, self.frm_player)
        self.lbl_player_score['text'] = f'Player score: {self.gamestate.get_player_score()}'
        if self.gamestate.player_bust():
            self.lbl_status['text'] = 'Player busts, Dealer wins!'
            self.enable_restart()

    def stand(self):
        self.bofunctions.destroy_widgets_in_frame(self.frm_dealer)
        self.gamestate.stand()
        for card in self.gamestate.cards_dealer:
            self.bofunctions.print_filled_card(card, self.frm_dealer)
        self.lbl_dealer_score['text'] = f'Dealer score: {self.gamestate.get_dealer_score()}'
        self.bofunctions.print_stand_result(self.gamestate, self.lbl_status)
        self.enable_restart()
    
    def first_phase_check_blackjack(self):
        if self.gamestate.get_player_score() == 21:
            self.lbl_status['text'] = 'Player wins by BlackJack!'
            self.enable_restart()
    
    def enable_restart(self):
        self.bofunctions.destroy_widgets_in_frame(self.frm_btns)
        tk.Button(master=self.frm_btns, text='New game', command=self.run_restart).grid(row=0, column=0, columnspan=2, sticky='ew')
    
    def run_restart(self):
        self.bofunctions.destroy_widgets_in_frame(self.frm_btns)
        self.lbl_player_score['text'] = ''
        self.lbl_dealer_score['text'] = ''
        self.lbl_status['text'] = 'Make your choice by either Hitting or Standing!'
        self.btns_create_and_config()
        self.gamestate = self.bofunctions.setup()
        self.game_setup()
        
if __name__ == "__main__":
    root = tk.Tk()
    ApplicationWindow(root).grid(sticky="nsew")
    root.mainloop()