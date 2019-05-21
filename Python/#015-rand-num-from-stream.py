from random import random

nums_seen_so_far = 0
result = None


def random_el(x):
    """
    Given a stream of elements too large to store in memory,
    pick a random element from the stream with uniform probability.
    """
    global nums_seen_so_far, result
    nums_seen_so_far += 1

    if nums_seen_so_far == 1:
        result = x
    else:
        random_value = int(nums_seen_so_far * random())
        if random_value == nums_seen_so_far - 1:
            result = x

    return result


if __name__ == '__main__':
    stream = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for index, element in enumerate(stream):
        random_element = random_el(element)
        print("Random element of the first {} numbers is {}".format(
            index + 1, random_element))
