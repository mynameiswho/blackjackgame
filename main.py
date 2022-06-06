import tkinter as tk
from game import BlackJackGame
from cards import generate_card_deck
import time

def print_state(gamestate):
    #Clear frames
    for frm in [frm_dealer, frm_player]:
        for child in frm.winfo_children():
            child.destroy()

    #Print dealer cards
    for idx, card in enumerate(gamestate.dealer_cards):
        if idx == 1 and len(gamestate.dealer_cards) == 2:
            tk.Label(master=frm_dealer,
            text='\n\n\n\n',
            font=('Arial', 18),
            width=5,
            relief=tk.GROOVE,
            borderwidth=2).pack(side=tk.LEFT, padx=10)
            break

        tk.Label(master=frm_dealer,
            text=f'\n{card.suit}\n\n{card.value}\n',
            font=('Arial', 18),
            width=5,
            relief=tk.GROOVE,
            borderwidth=2).pack(side=tk.LEFT, padx=10)
        if len(gamestate.dealer_cards) == 2:
            pass
        else:
            tk.Label(master=w, text=f'Dealer score: {gamestate.dealer_score}').grid(row=0, sticky='s', padx=10, pady=10)

    #Print player cards
    for card in gamestate.player_cards:
        tk.Label(master=frm_player,
            text=f'\n{card.suit}\n\n{card.value}\n',
            font=('Arial', 18),
            width=5,
            relief=tk.GROOVE,
            borderwidth=2).pack(side=tk.LEFT, padx=10)
        tk.Label(master=w, text=f'Player score: {gamestate.player_score}').grid(row=1, sticky='s', padx=10, pady=10)

def hit(gamestate):
    gamestate.hit()
    print_state(gamestate)

    #Check if player busts
    if gamestate.player_score > 21:
        for child in frm_player.winfo_children():
            child.destroy()
        tk.Label(master=frm_player, text='Player busts, Dealer wins!', font=('Arial', 18)).grid(row=0, column=0)
        return

    #Check if player got blackjack
    if gamestate.player_score == 21:
        for child in frm_player.winfo_children():
            child.destroy()
        tk.Label(master=frm_player, text='Player wins by BlackJack!', font=('Arial', 18)).grid(row=0, column=0)
        return

def stand(gamestate):
    gamestate.stand()
    print_state(gamestate)

    #Check if dealer busts
    if gamestate.dealer_score > 21:
        for child in frm_player.winfo_children():
            child.destroy()
        tk.Label(master=frm_player, text='Dealer busts, Player wins!', font=('Arial', 18)).grid(row=0, column=0)
        return
    
    #Check if dealer won
    if gamestate.dealer_score > gamestate.player_score:
        for child in frm_player.winfo_children():
            child.destroy()
        tk.Label(master=frm_player, text='Dealer wins!', font=('Arial', 18)).grid(row=0, column=0)
        return
    
    #Check if player won
    if gamestate.dealer_score < gamestate.player_score:
        for child in frm_player.winfo_children():
            child.destroy()
        tk.Label(master=frm_player, text='Player wins!', font=('Arial', 18)).grid(row=0, column=0)
        return
    
    #Check if tie
    if gamestate.dealer_score == gamestate.player_score:
        for child in frm_player.winfo_children():
            child.destroy()
        tk.Label(master=frm_player, text='Tie game!', font=('Arial', 18)).grid(row=0, column=0)
        return

#Create GUI
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
btn_hit = tk.Button(master=frm_btns, text='Hit', command= lambda: hit(gamestate))
btn_stand = tk.Button(master=frm_btns, text='Stand', command= lambda: stand(gamestate))

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

#Initial setup
deck = generate_card_deck()
gamestate = BlackJackGame(deck)
gamestate.setup()

print_state(gamestate)

w.mainloop()