import pytest
from give_bmi import give_bmi, apply_limit

valid_height_int = [1, 2, 1, 1, 2]
valid_weight_int = [89, 130, 77, 87, 56]

height_float_same_size = [1.805, 1.772, 1.668, 1.55, 1.78]
weight_float_same_size = [89.1, 130.5, 77.8, 87.0, 56.4]

height_diff_size = [1.77, 1.80, 1.77, 1.66, 1.55, 1.78]
weight_diff_size = [89, 130, 77]

height_neg_values = [22, -177, 166, -155, 88]
weight_neg_values = [-89, 890, -77, 777, -56]

height_zero_values = [180, 177, 0, 155, 178]
weight_zero_values = [89, 130, 77, 87, 0]

height_incorrect_values = [False, -177, 166, -155, 0]
weight_incorrect_values = ["a", 130, [77], 87, 56]

limit_bmi_valid = [
    27,
    41.56072132851632,
    27.963240918056922,
    36.21227887617065,
    17.80078272945335,
]

limit_bmi_zero = [
    0,
    41.56072132851632,
    27.963240918056922,
    36.21227887617065,
    17.80078272945335,
]

limit_bmi_neg = [
    -27,
    41.56072132851632,
    27.963240918056922,
    36.21227887617065,
    17.80078272945335,
]

limit_bmi_invalid = [
    "a",
    41.56072132851632,
    27.963240918056922,
    36.21227887617065,
    17.80078272945335,
]


def test_happy_path():
    assert give_bmi(valid_height_int, valid_weight_int) == [
        89.0,
        32.5,
        77.0,
        87.0,
        14.0,
    ]
    assert give_bmi(height_float_same_size, weight_float_same_size) == [
        27.347856446773733,
        41.56072132851632,
        27.963240918056922,
        36.21227887617065,
        17.80078272945335,
    ]


# TESTING GIVE_BMI FUNCTION
def test_different_size():
    with pytest.raises(ValueError):
        give_bmi(valid_height_int, weight_diff_size)
    with pytest.raises(ValueError):
        give_bmi(height_diff_size, valid_weight_int)


def test_zero_values():
    with pytest.raises(ValueError):
        give_bmi(valid_height_int, weight_zero_values)
    with pytest.raises(ValueError):
        give_bmi(height_zero_values, valid_weight_int)


def test_neg_values():
    with pytest.raises(ValueError):
        give_bmi(valid_height_int, weight_neg_values)
    with pytest.raises(ValueError):
        give_bmi(height_neg_values, valid_weight_int)


def test_neg_and_zero_values():
    with pytest.raises(ValueError):
        give_bmi(height_zero_values, weight_neg_values)
    with pytest.raises(ValueError):
        give_bmi(height_neg_values, weight_zero_values)


def test_incorrect_values():
    with pytest.raises(ValueError):
        give_bmi(valid_height_int, weight_incorrect_values)
    with pytest.raises(ValueError):
        give_bmi(height_incorrect_values, valid_weight_int)


# TESTING APPLY_LIMIT FUNCTION
def test_limit_happy_path():
    assert apply_limit(limit_bmi_valid, 27) == [False, True, True, True, False]


def test_limit_zero():
    with pytest.raises(ValueError):
        apply_limit(limit_bmi_zero, 27)


def test_limit_neg_values():
    with pytest.raises(ValueError):
        apply_limit(limit_bmi_neg, 27)
    with pytest.raises(ValueError):
        apply_limit(limit_bmi_valid, -27)


def test_limit_invalid_values():
    with pytest.raises(ValueError):
        apply_limit(limit_bmi_invalid, 27)
    with pytest.raises(ValueError):
        apply_limit(limit_bmi_valid, "a")
