import pytest

# Function to test square
def square(num):
    return num ** 2

# Function to test cube
def cube(num):
    return num ** 3

# Tests for square
def test_square():
    assert square(2) == 4, "Test Failed: Square of 2 should be 4"
    assert square(3) == 9, "Test Failed: Square of 3 should be 9"

# Tests for cube
def test_cube():
    assert cube(2) == 8, "Test Failed: Cube of 2 should be 8"
    assert cube(3) == 27, "Test Failed: Cube of 3 should be 27"

# Test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("String")
    with pytest.raises(TypeError):
        cube("Text")
