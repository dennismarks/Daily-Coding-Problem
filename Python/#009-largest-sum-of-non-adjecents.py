def largest_sum_of_non_adjacents(A):
    """
    Given a list of integers, write a function that returns the largest sum
    of non-adjacent numbers. Numbers can be 0 or negative.

    For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
    [5, 1, 1, 5] should return 10, since we pick 5 and 5.

    Follow-up: Can you do this in O(N) time and constant space?
    """
    incl = A[0]     # max sum I can get incluading this number
    excl = 0        # max sum I can get excluading this number

    for i in range(1, len(A)):
        new_excl = max(incl, excl + A[i])
        excl = incl
        incl = new_excl

    return max(incl, excl)


if __name__ == '__main__':
    assert largest_sum_of_non_adjacents([2, 4, 6, 2, 5]) == 13
    assert largest_sum_of_non_adjacents([5, 1, 1, 5]) == 10
    assert largest_sum_of_non_adjacents([5, 1, 2, 5, 3, 2]) == 12
