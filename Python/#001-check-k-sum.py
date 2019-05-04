def check_pair_sum(array, k):
    """
    Given a list of numbers and a number k, return whether any two numbers from
    the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

    Bonus: Can you do this in one pass?
    """
    solutions = set()
    for number in array:
        if number in solutions:
            return True
        solutions.add(k - number)
    return False


if __name__ == '__main__':
    assert check_pair_sum([10, 15, 3, 7], 17)
