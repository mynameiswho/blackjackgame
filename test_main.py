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



if __name__ == '__main__':
    pytest.main()