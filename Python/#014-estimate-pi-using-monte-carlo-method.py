from random import random


def estimate_pi(num_of_tests):
    """
    The area of a circle is defined as πr^2. Estimate π to 3 decimal places
    using a Monte Carlo method.

    Hint: The basic equation of a circle is x^2 + y^2 = r^2.
    """
    circle_points = 0

    for _ in range(num_of_tests):
        x = random()
        y = random()
        if x*x + y*y <= 1:
            circle_points += 1

    return 4 * (circle_points / num_of_tests)
