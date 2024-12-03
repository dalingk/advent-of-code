import pytest

from multiply import get_mult_enable_groups
from multiply import get_multiplication_groups


@pytest.mark.parametrize(
    "input_text,result",
    [
        ("mul(44,46)", [(44, 46)]),
        ("mul(123,4)", [(123, 4)]),
    ],
)
def test_get_multiplication_groups(input_text, result):
    assert get_multiplication_groups(input_text) == result


@pytest.mark.parametrize(
    "input_text,result",
    [
        ("do()mul(44,46)don't()mul(2,2)", [(44, 46)]),
    ],
)
def test_get_mult_enable_groups(input_text, result):
    assert get_mult_enable_groups(input_text) == result
