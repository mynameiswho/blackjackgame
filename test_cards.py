import pytest
from cards import Card
from cards import generate_card_deck

def test_cardclass():
    spade = '\u2664'
    deck_value = 'K'
    game_value = 10
    assert Card(spade, deck_value, game_value).game_value == 10

def test_generate_card_deck():
    deck = generate_card_deck()
    assert len(deck) == 52

if __name__ == '__main__':
    pytest.main()