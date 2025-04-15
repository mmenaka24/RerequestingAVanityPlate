from plates import is_valid


def test_is_valid_starts_with_two_letters():
    assert is_valid("MM") == True
    assert is_valid("MENAKA") == True
    assert is_valid("M24") == False
    assert is_valid("1M") == False
    assert is_valid("!M") == False


def test_is_valid_max_six_min_two():
    assert is_valid("M") == False
    assert is_valid("MM") == True
    assert is_valid("MNK") == True
    assert is_valid("MEMA") == True
    assert is_valid("MARUT") == True
    assert is_valid("MENAKA") == True
    assert is_valid("MENAKAM") == False
    assert is_valid("MENAKAMARU") == False


def test_is_valid_numbers_at_end():
    assert is_valid("MENAKA") == True
    assert is_valid("MM024") == False
    assert is_valid("MM24") == True
    assert is_valid("MM240") == True
    assert is_valid("MM24MM") == False


def test_is_valid_no_punct():
    assert is_valid("MENAKA") == True
    assert is_valid("MM!") == False
    assert is_valid("MM MM") == False
    assert is_valid("MM.MM") == False
    assert is_valid("MM-MM") == False
    assert is_valid("MM@12") == False
