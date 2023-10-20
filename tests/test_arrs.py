from utils.arrs import get_, my_slice
import pytest


def test_get():
    assert get_([1, 2, 3], 1, "test") == 2
    assert get_([], 0, "test") == "test"


def test_slice():
    assert my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert my_slice([1, 2, 3], 1) == [2, 3]

