import pytest


class NotInRange(Exception):
    def __init__(self, message="value not in range"):
        self.message = message
        super().__init__(self.message)


def test_generic():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10, 22):
            raise NotInRange
    # a = 'sd'
    # b = 'sd'
    # assert a == b # when pytest is run this gets checked

# make sure the function start with 'test_' otherwise pytest will not run them


def test_function():
    a = 4
    b = 4
    assert a == b
