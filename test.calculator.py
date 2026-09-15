from calculator import subtract

def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6

def test_subtract_negative_numbers():
    assert subtract(-1, -1) == 0

print("test_subtract_positive_numbers")
print("test_subtract_negative_numbers")