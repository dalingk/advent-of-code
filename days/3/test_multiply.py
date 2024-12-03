import pytest

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
