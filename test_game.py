import pytest
from regex import B
from cards import generate_card_deck
from cards import Card
from game import BlackJackGameMechanics

@pytest.fixture
def BJGM_setup() -> BlackJackGameMechanics:
    d = generate_card_deck()
    BJGM_setup = BlackJackGameMechanics(d)
    return BJGM_setup

def test_run_first_phase(BJGM_setup: BlackJackGameMechanics):
    BJGM_setup.first_deal()
    assert len(BJGM_setup.cards_player) == 2
    assert len(BJGM_setup.cards_dealer) == 2

def test_hit(BJGM_setup: BlackJackGameMechanics):
    bef_deck_length = len(BJGM_setup.deck)
    bef_player_card_length = len(BJGM_setup.cards_player)
    bef_player_score = BJGM_setup.get_player_score()
    
    BJGM_setup.hit()
    
    assert len(BJGM_setup.deck) == bef_deck_length - 1
    assert len(BJGM_setup.cards_player) == bef_player_card_length + 1
    
    last_card_idx = len(BJGM_setup.cards_player) - 1
    assert BJGM_setup.get_player_score() == bef_player_score + BJGM_setup.cards_player[last_card_idx].game_value

def test_stand(BJGM_setup: BlackJackGameMechanics):
    BJGM_setup.stand()

    last_card_idx = len(BJGM_setup.cards_dealer) - 1
    last_card = BJGM_setup.cards_dealer[last_card_idx]
    limit_to_dealing_new = 17
    score_before_last_dealt_card = BJGM_setup.get_dealer_score() - last_card.game_value

    assert limit_to_dealing_new > score_before_last_dealt_card

def test_deal_to_player(BJGM_setup: BlackJackGameMechanics):
    cards_bef_deal = len(BJGM_setup.cards_player)
    deck_bef_deal = len(BJGM_setup.deck)

    BJGM_setup._deal_to_player()

    assert len(BJGM_setup.cards_player) == cards_bef_deal + 1
    assert len(BJGM_setup.deck) == deck_bef_deal - 1

def test_deal_to_dealer(BJGM_setup: BlackJackGameMechanics):
    #Arrange
    cards_bef_deal = len(BJGM_setup.cards_dealer)
    deck_bef_deal = len(BJGM_setup.deck)

    #Act
    BJGM_setup._deal_to_dealer()

    #Assert
    assert len(BJGM_setup.cards_dealer) == cards_bef_deal + 1
    assert len(BJGM_setup.deck) == deck_bef_deal - 1

def test_check_if_two_aces(BJGM_setup: BlackJackGameMechanics):
    #Arrange
    ace_spades = Card('u\2664', 'A', 11)
    ace_hearts = Card('u\2661', 'A', 11)
    ace_list = [ace_spades, ace_hearts]

    #Act
    assert BJGM_setup._check_if_two_aces(ace_list) == True

def test_check_if_ace_and_bust(BJGM_setup: BlackJackGameMechanics):
    #Arrange
    ace_spades = Card('u\2664', 'A', 11)
    king_spades = Card('u\2664', 'K', 10)
    score = 22

    #Act + Assert
    assert BJGM_setup._check_if_ace_and_bust(ace_spades, score) == True
    assert BJGM_setup._check_if_ace_and_bust(king_spades, score) == False


if __name__ == '__main__':
    pytest.main()