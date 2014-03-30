from django.test import TestCase
from solve.models import Equation


class EquationTestCase(TestCase):

    def test_equation_creation(self):
        """
        Test equation creation, it should store the result of the equation
        each time the model is saved
        """
        equation = Equation.objects.create(equation="1+1")
        self.assertEqual(equation.result, 2.0)
        self.assertTrue(equation.valid)

    def test_equation_with_syntax_error(self):
        """
        Test equation when, the expresion (equation) has a syntax error.
        In the result we should store the exception and the the valid flag
        should be updated
        """
        exp = "wrong equation"
        equation = Equation.objects.create(equation=exp)
        self.assertIn(u'invalid syntax', equation.result)
        self.assertFalse(equation.valid)

    def test_session_in_equation(self):
        """
        Test if there's a session in the equation
        """
        equation = Equation.objects.create(equation="1+1")
        self.assertEqual(equation.session.name, "")
        self.assertEqual(equation.session.user, None)
