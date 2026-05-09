import src.lab_j as lab_j


def test_turn_right():
    result = lab_j.turn_right("N")

    if result == "E":
        assert True
    else:
        assert False


def test_turn_left():
    result = lab_j.turn_left("N")

    if result == "W":
        assert True
    else:
        assert False
