from square_number import square

def test_positive_num():
    assert square(2) == 4
    assert square(3) == 9

def test_negative_num():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
