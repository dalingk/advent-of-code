import pytest
from calibration import is_valid_equation
from calibration import load_file

CONTENT = """190: 10 19
3267: 81 40 27
"""


@pytest.mark.parametrize(
    "test_value,equation,result",
    [
        (190, [10, 19], True),
        (3267, [81, 40, 27], True),
        (83, [17, 5], False),
        (156, [15, 6], True),
        (7290, [6, 8, 6, 15], True),
        (161011, [16, 10, 13], False),
        (192, [17, 8, 14], True),
        (21037, [9, 7, 18, 13], False),
        (292, [11, 6, 16, 20], True),
    ],
)
def test_is_valid_equation(test_value, equation, result):
    assert is_valid_equation(test_value, equation) == result


def test_load_file(tmp_path):
    input_file = tmp_path / "input.txt"
    input_file.write_text(CONTENT)
    assert load_file(input_file) == [(190, [10, 19]), (3267, [81, 40, 27])]
