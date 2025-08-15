"""Tests for the say_hi app"""

# Run the tests with: pytest tests/test_app.py
from ..app import add_numbers

"""Test that add_numbers correctly sums two numbers"""
def test_add_numbers():
    assert 3 == add_numbers(1,2)
