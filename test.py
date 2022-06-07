from game import BlackJackGame
from cards import generate_card_deck

d = generate_card_deck()
g = BlackJackGame(d)
g.setup()

print(g.player_score)
for card in g.player_cards:
    print(f'{card.suit}{card.value}')
g.hit()