# The standard form of a quadratic equation is:

# ax2 + bx + c = 0, where
# a, b and c are real numbers and
# a ≠ 0

# The solutions of this quadratic equation is given by:

#(-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 4
b = 6
c = 8

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))