import pytest
from working import convert

# Test correct conversions
def test_correct_conversions():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:45 AM") == "22:30 to 08:45"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1:15 AM to 11:45 PM") == "01:15 to 23:45"

# Test invalid inputs that should raise ValueError
def test_invalid_inputs():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")  # Invalid minutes
    with pytest.raises(ValueError):
        convert("13:00 PM to 14:00 AM")  # Invalid hours
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # Missing 'to'
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")  # Incorrect format
    with pytest.raises(ValueError):
        convert("25:00 AM to 5:00 PM")  # Invalid hour
    with pytest.raises(ValueError):
        convert("10:30 XM to 8:30 YM")  # Invalid AM/PM
    with pytest.raises(ValueError):
        convert("9:00AM to 5:00PM")  # Missing space before AM/PM

# Test handling of missing minutes
def test_missing_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

# Test edge cases
def test_edge_cases():
    assert convert("12:01 AM to 11:59 PM") == "00:01 to 23:59"
    assert convert("1 AM to 11 PM") == "01:00 to 23:00"
    assert convert("12 PM to 1 PM") == "12:00 to 13:00"
    assert convert("11:59 AM to 12:01 PM") == "11:59 to 12:01"

