from freq_count import *
import pytest


@pytest.mark.parametrize('inp, res', [
    ("a bb ccc", "cccbba"),
    ("hh b zzz 454", "zzzhh44b5"),
    ("11 222 5", "222115"),
    ("!!!!!####$$$$$$$%%%%&&*(*)*()", "$$$$$$$!!!!!####%%%%***&&()()")
])
def test_counter_freq_a_is_correct(inp, res):
    assert freq_counter_a(inp) == res


@pytest.mark.parametrize('inp, res', [
    ("a bb ccc", "cba"),
    ("hh b zzz 454", "zh4b5"),
    ("11 222 5", "215"),
    ("!!!!!####$$$$$$$%%%%&&*(*)*()", "$!#%*&()")
])
def test_counter_freq_b_is_correct(inp, res):
    assert freq_counter_b(inp) == res


@pytest.mark.parametrize('inp, res', [
    ("Happy HH", "HHHaypp"),
    ("BaBak", "bbaak"),
    (" 33 8 0", "3380   ")
])
def test_counter_freq_a_is_wrong(inp, res):
    assert freq_counter_a(inp) != res


@pytest.mark.parametrize('inp, res', [
    ("a bb ccc", "cccbba"),
    ("x y z ", "xyz   "),
])
def test_counter_freq_b_is_wrong(inp, res):
    assert freq_counter_b(inp) != res


def test_counter_freq_a_handle_exception():
    assert freq_counter_a(12345) is None


def test_counter_freq_b_handle_exception():
    assert freq_counter_b(45632) is None


# testing to make sure it does raise an exception
def test_counter_freq_a_raise_exception():
    with pytest.raises(TypeError) as e:
        freq_counter_a(12123123 + "453453")


def test_counter_freq_b_raise_exception():
    with pytest.raises(TypeError) as e:
        freq_counter_b(879787 + "-=65756")
