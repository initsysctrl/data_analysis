from sympy import solve, sin, cos, pprint
from sympy.abc import x, y
from sympy.plotting import plot
import numpy as np


sol = solve(x**2+2*x+5, x)
pprint(sol)
plot(sin(x))
