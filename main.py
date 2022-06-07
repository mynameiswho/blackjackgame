import tkinter as tk
from game import BlackJackGame
from cards import generate_card_deck

def initial_setup():
    deck = generate_card_deck()
    gamestate = BlackJackGame(deck)
    gamestate.setup()
    print_state(gamestate)
    return gamestate

def print_state(gamestate, first_run=1, hit=0):
    #Clear frames
    for frm in [frm_dealer, frm_player]:
        for child in frm.winfo_children():
            child.destroy()

    #Print dealer cards
    for idx, card in enumerate(gamestate.dealer_cards):
        #Hide 2nd card if: 1st run or hit
        if (first_run == 1 or hit == 1) and idx == 1:
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
        
    #Hide Dealer score on 1st run
    if first_run == 1 or hit == 1:
        pass
    else:
        lbl_dealer_score['text'] = f'Dealer score: {gamestate.dealer_score}'

    #Print player cards
    for card in gamestate.player_cards:
        tk.Label(master=frm_player,
            text=f'\n{card.suit}\n\n{card.value}\n',
            font=('Arial', 18),
            width=5,
            relief=tk.GROOVE,
            borderwidth=2).pack(side=tk.LEFT, padx=10)

    lbl_player_score['text'] = f'Player score: {gamestate.player_score}'
    
    #Check if player got Blackjack on 1st run
    if first_run == 1:
        if gamestate.player_score == 21:
            lbl_status['text'] = 'Player wins by BlackJack!'
            enable_restart()
            return

def hit(gamestate):
    gamestate.hit()
    print_state(gamestate, first_run=0, hit=1)

    #Check if player busts
    if gamestate.player_score > 21:
        lbl_status['text'] = 'Player busts, Dealer wins!'
        enable_restart()
        return

def stand(gamestate):
    gamestate.stand()
    print_state(gamestate, first_run=0)

    #Check if dealer busts
    if gamestate.dealer_score > 21:
        lbl_status['text'] = 'Dealer busts, Player wins!'
        enable_restart()
        return
    
    #Check if dealer won
    if gamestate.dealer_score > gamestate.player_score:
        lbl_status['text'] = 'Dealer beats Player, Dealer wins!'
        enable_restart()
        return
    
    #Check if player won
    if gamestate.dealer_score < gamestate.player_score:
        lbl_status['text'] = 'Player beats Dealer, Player wins!'
        enable_restart()
        return
    
    #Check if tie
    if gamestate.dealer_score == gamestate.player_score:
        lbl_status['text'] = 'Tie game!'
        enable_restart()
        return

def enable_restart():
    #Delete all widgets in frm_btns
    for widget in frm_btns.winfo_children():
        widget.destroy()
    
    #Create new button and place
    tk.Button(master=frm_btns, text='New game', command= run_restart).grid(row=0, column=0, columnspan=2, sticky='ew')
    
def run_restart():
    #Delete all widgets in frm_btns
    for widget in frm_btns.winfo_children():
        widget.destroy()
    
    #Replace texts
    lbl_dealer_score['text'] = 'Dealer score: '
    lbl_player_score['text'] = 'Player score: '
    lbl_status['text'] = 'Make your choice by either Hitting or Standing!'
    
    #Buttons
    btn_hit = tk.Button(master=frm_btns, text='Hit', command= lambda: hit(gamestate))
    btn_stand = tk.Button(master=frm_btns, text='Stand', command= lambda: stand(gamestate))
    
    #Place old buttons back in frm_btns
    btn_hit.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
    btn_stand.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

    gamestate = initial_setup()

#Create GUI
w = tk.Tk()
w.title('Simple BlackJack Game')
w.rowconfigure([0,1], minsize=200)
w.rowconfigure([2, 3], minsize=50)
w.columnconfigure(0, minsize=75)
w.columnconfigure(1, minsize=500)

#Frames
frm_dealer = tk.Frame(master=w, relief=tk.SUNKEN, borderwidth=3, background='white')
frm_player = tk.Frame(master=w, relief=tk.SUNKEN, borderwidth=3, background='white')
frm_status = tk.Frame(master=w, background='white')
frm_btns = tk.Frame(master=w)

#Labels
lbl_dealer = tk.Label(master=w, text='DEALER')
lbl_dealer_score = tk.Label(master=w, text= 'Dealer score: ')
lbl_player = tk.Label(master=w, text='PLAYER')
lbl_player_score = tk.Label(master=w, text= 'Player score: ')
lbl_status = tk.Label(master=frm_status, text='Make your choice by either Hitting or Standing!')

#Buttons
btn_hit = tk.Button(master=frm_btns, text='Hit', command= lambda: hit(gamestate))
btn_stand = tk.Button(master=frm_btns, text='Stand', command= lambda: stand(gamestate))

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

#Initial setup
gamestate = initial_setup()

w.mainloop()