from sympy.parsing.sympy_parser import parse_expr
from django.conf import settings

ROUND_NDIGIT = getattr(settings, 'ROUND_NDIGIT', 10)

def solve(exp):
    """
    Given exp, make the calculations needed and return the value as float
    """
    value = parse_expr(exp).evalf()
    return round(value, ROUND_NDIGIT)