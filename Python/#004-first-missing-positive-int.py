def first_missing_pos_int(array):
    """
    Given an array of integers, find the first missing positive integer in
    linear time and constant space. In other words, find the lowest positive
    integer that does not exist in the array. The array can contain duplicates
    and negative numbers as well.

    You can modify the input array in-place.
    """
    n = max(array)
    if n < 1:
        return 1
    if len(array) == 1:
        return 2 if array[0] == 1 else 1

    my_array = [0] * n
    # set value at index i to 1 if such value exists in array
    for i in range(len(array)):
        if array[i] > 0:
            my_array[array[i] - 1] = 1

    j = 0
    # return first occurence of zero
    for j in range(len(my_array)):
        if my_array[j] == 0:
            return j + 1

    return j + 2


def first_missing_pos_int_using_set(array):
    my_set = set(array)
    for i in range(1, len(array)):
        if (i in my_set) and (i + 1 not in my_set):
            return i + 1


if __name__ == '__main__':
    assert first_missing_pos_int([3, 4, -1, 1]) == 2
    assert first_missing_pos_int([1, 2, 0]) == 3

    assert first_missing_pos_int_using_set([3, 4, -1, 1]) == 2
    assert first_missing_pos_int_using_set([1, 2, 0]) == 3
