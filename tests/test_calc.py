from app.calculator import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_substraction_success(self):
        assert self.calc.subtraction(self, 5, 3) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(self, 1, 3) == 3

    def test_division_success(self):
        assert self.calc.division(self, 4, 2) == 2