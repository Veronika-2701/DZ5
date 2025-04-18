import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),
    ("hello world   ", "hello world   "),
    ("   python  ", "python  "),
    ("you", "you")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", "")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    ("skypro", "s"),
    ("hello", "ll"),
    ("python", "t"),
    ("Veronika", "on"),
    ("poop loud", " "),
    ("2701Ver", "27")
])
def test_contains_positive(input_str, symbol):
    assert string_utils.contains(input_str, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    ("skypro", "e"),
    ("hello", "hl"),
    ("python", "l"),
    ("Veronika", "/7"),
    ("рooр  loud", "poop"),
    ("2701Ver", "Vr")
])
def test_contains_negative(input_str, symbol):
    assert string_utils.contains(input_str, symbol) is False


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, result", [
    ("skypro", "sky", "pro"),
    ("hello world", "hello ", "world"),
    ("python", "pyth", "on"),
    ("yourself", "your", "self"),
    ("123456789", "4567", "12389"),
    ("loop953", "op9", "lo53")
])
def test_delete_symbol_positive(input_str, symbol, result):
    assert string_utils.delete_symbol(input_str, symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, result", [
    ("skypro", "sp", "skypro"),
    ("hello world", "tuk", "hello world"),
    ("python", "34", "python"),
    ("yourself", "poop9", "yourself"),
    ("123456789", "you", "123456789"),
    ("loop953", " ", "loop953")
])
def test_delete_symbol_negative(input_str, symbol, result):
    assert string_utils.delete_symbol(input_str, symbol) == result
