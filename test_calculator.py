import pytest as pytest

from Calculator import Calculator


class TestCalculator:

    @pytest.fixture()
    def calculator(self):
        return Calculator()

    def test_add_number(self, calculator):
        print("Testing Add method")
        result = calculator.add_two_numbers(2, 2)
        assert result == 4

    def test_subtract_number(self, calculator):
        print("Testing Add method")
        result = calculator.subtract_two_numbers(2, 2)
        assert result == 0

    def test_multiply_number(self, calculator):
        print("Testing Add method")
        result = calculator.multiply_two_numbers(2, 2)
        assert result == 4

    def test_divide_number(self, calculator):
        print("Testing Add method")
        result = calculator.divide_two_numbers(2, 2)
        assert result == 1.0
