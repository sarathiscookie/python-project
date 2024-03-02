from linear_search import locate_card

def test_card_not_matching():
    query = 11

    cards = [10, 9, 8, 7, 6, 5, 3, 2, 1]

    assert locate_card(cards, query) == -1

def test_card_matching():
    query = 7

    cards = [10, 9, 8, 7, 6, 5, 3, 2, 1]

    assert locate_card(cards, query) == 7