def staircase_unique_ways(num_of_steps):
    """
    There exists a staircase with N steps, and you can climb up either 1 or 2
    steps at a time. Given N, write a function that returns the number of
    unique ways you can climb the staircase. The order of the steps matters.

    For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2
    """
    if num_of_steps == 0 or num_of_steps == 1:
        return 1

    nums = [None for _ in range(num_of_steps + 1)]
    nums[0] = 1
    nums[1] = 1

    for i in range(2, num_of_steps + 1):
        nums[i] = nums[i-1] + nums[i-2]

    return nums[num_of_steps]


def staircase_unique_ways_2(num_of_steps, step_sizes):
    """
    What if, instead of being able to climb 1 or 2 steps at a time, you
    could climb any number from a set of positive integers X? For example,
    if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
    """
    if num_of_steps == 0:
        return 1

    nums = [None for _ in range(num_of_steps + 1)]
    nums[0] = 1

    for i in range(1, num_of_steps + 1):
        total = 0
        for j in step_sizes:
            if i - j >= 0:
                total += nums[i - j]
        nums[i] = total

    return nums[num_of_steps]


if __name__ == '__main__':
    assert staircase_unique_ways(4) == 5
    assert staircase_unique_ways_2(4, {1, 3, 5}) == 3



