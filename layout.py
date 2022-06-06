import tkinter as tk
import random
from cards import generate_card_deck

'''
1. Create 3 frames - Dealer, Player, Buttons
    Label each frame
2. Build dynamic updating columns - nope, pack
'''

def blackjack_game(deck):
    
    global cards_values

    player_cards = []
    dealer_cards = []

    player_score = 0
    dealer_score = 0

    while len(player_cards) < 2:
        #Deal random cards
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)
        player_score += player_card.card_value
        
        #Handle if both cards are ace
        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10

def blackjack_window():
    w = tk.Tk()
    w.title('Simple BlackJack Game')
    w.rowconfigure([0,1], minsize=200)
    w.rowconfigure(2, minsize=100)
    w.columnconfigure(0, minsize=75)
    w.columnconfigure(1, minsize=500)

    #Frames
    frm_dealer = tk.Frame(master=w, relief=tk.SUNKEN, borderwidth=3)
    frm_player = tk.Frame(master=w, relief=tk.SUNKEN, borderwidth=3)
    frm_btns = tk.Frame(master=w)

    #Labels
    lbl_dealer = tk.Label(master=w, text='DEALER')
    lbl_player = tk.Label(master=w, text='PLAYER')

    #Buttons
    btn_hit = tk.Button(master=frm_btns, text='Hit')
    btn_stand = tk.Button(master=frm_btns, text='Stand')

    #Layout frames
    frm_dealer.grid(row=0, column=1, sticky='nsew')
    frm_player.grid(row=1, column=1, sticky='nsew')
    frm_btns.grid(row=2, column=1, sticky='nsew')
    frm_btns.rowconfigure(0, weight=1)
    frm_btns.columnconfigure([0, 1], weight=1)

    #Layout labels
    lbl_dealer.grid(row=0, sticky='ew')
    lbl_player.grid(row=1, sticky='ew')

    #Layout buttons
    btn_hit.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
    btn_stand.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

    tk.Label(master=frm_player,
        text='\n\u2664\n\n2\n',
        font=('Arial', 18),
        width=5,
        relief=tk.GROOVE,
        borderwidth=2).pack(side=tk.LEFT, padx=10)

    w.mainloop()

blackjack_window()