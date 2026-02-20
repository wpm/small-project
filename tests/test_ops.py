from small_project import add, concat


# Tests for add(a, b)

def test_add_integers():
    assert add(2, 3) == 5


def test_add_floats():
    assert add(1.5, 2.5) == 4.0


def test_add_negative_numbers():
    assert add(-4, 6) == 2


def test_add_negative_result():
    assert add(-10, 3) == -7


# Tests for concat(a, b)

def test_concat_two_nonempty_strings():
    assert concat("hello", "world") == "helloworld"


def test_concat_empty_left():
    assert concat("", "world") == "world"


def test_concat_empty_right():
    assert concat("hello", "") == "hello"


def test_concat_both_empty():
    assert concat("", "") == ""
