import pytest
from unittest.mock import patch
from io import StringIO
from array2D import slice_me

family_valid = [[1.80, 78.4], [10, 102.7], [2.10, 98.5], [1.88, 75.2]]
family_wrong_size = [[1.80, 78.4], [102.7], [2.10, 98.5], [1.88, 75.2]]

def test_slice_me_print():
    expected_output = "My shape is : (4, 2)\nMy new shape is : (2, 2)\n"
    expected_result = [[1.80, 78.4], [10, 102.7]]

    # Patch capture the result in a string...
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        result = slice_me(family_valid, 0, 2)
        # !... which we can get the result from
        actual_output = mock_stdout.getvalue()

    # Assert the printed output matches the expected value
    assert actual_output == expected_output
    assert result == expected_result

def test_wrong_size_list():
    with pytest.raises()
