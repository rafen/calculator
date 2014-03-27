from math import log

from django.test import TestCase
from solve.calculator import solve, ROUND_NDIGIT


class SolveTestCase(TestCase):

    def _eval(self, exp):
        """
        Helper (inner) function to easly eval safe expresions
        """
        float_value = float(eval(exp))
        return round(float_value, ROUND_NDIGIT)

    def test_addition(self):
        """
        Test for addtion
        """
        self.assertEqual(solve("1+1"), 1 + 1)
        self.assertEqual(solve("10 +7"), 10 + 7)
        self.assertEqual(solve("1+-1"), 1 + -1)

    def test_subtraction(self):
        """
        Test for subtraction
        """
        self.assertEqual(solve("1-1"), 1 - 1)
        self.assertEqual(solve("10 -7"), 10 - 7)
        self.assertEqual(solve("1--1"), 1 - -1)

    def test_multiplication(self):
        """
        Test for multiplication
        """
        self.assertEqual(solve("1*1"), 1 * 1)
        self.assertEqual(solve("10 *7"), 10 * 7)
        self.assertEqual(solve("1*-1"), 1 * -1)

    def test_division(self):
        """
        Test for division
        """
        self.assertEqual(solve("1/1"), self._eval("1 / 1."))
        self.assertEqual(solve("10 /7"), self._eval("10 / 7."))
        self.assertEqual(solve("1/-1"), self._eval("1 / -1."))

    def test_logarithm(self):
        """
        Test for logarithm
        """
        self.assertEqual(solve("log(1)"), self._eval("log(1)"))
        self.assertEqual(solve("log(2)"), self._eval("log(2)"))

    def test_precedence(self):
        """
        Test for precedence
        """
        exp = "5*3*(8-23)"
        self.assertEqual(solve(exp), self._eval(exp))

    def test_precedence_and_combination(self):
        """
        Test the combination of several calculations
        """
        exp = "(2+2)*log(10)/3"
        self.assertEqual(solve(exp), self._eval(exp))

    def test_code_injection(self):
        """
        An exception should be raise if users try to inyect code in eval
        """
        exp = "__import__('os').system('echo hello, I am a command execution')"
        self.assertRaises(Exception, solve, exp)
