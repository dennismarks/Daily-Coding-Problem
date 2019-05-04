def product_array_division(array):
    """
    Given an array of integers, return a new array such that each element
    at index i of the new array is the product of all the numbers in the
    original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output
    would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the
    expected output would be [2, 3, 6].
    """
    product = 1
    for number in array:
        product *= number

    new_array = []
    for number in array:
        new_array.append(product // number)

    return new_array


def product_array(array):
    """
    Follow-up: what if you can't use division?
    """
    new_array = [1 for _ in array]
    product_on_the_left = [1 for _ in array]
    product_on_the_right = [1 for _ in array]

    for i in range(1, len(array)):
        product_on_the_left[i] = product_on_the_left[i - 1] * array[i - 1]

    for i in range(len(array) - 2, -1, -1):
        product_on_the_right[i] = product_on_the_right[i + 1] * array[i + 1]

    for i in range(len(array)):
        new_array[i] = product_on_the_left[i] * product_on_the_right[i]

    return new_array


if __name__ == '__main__':
    assert product_array_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert product_array([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]

    assert product_array_division([3, 2, 1]) == [2, 3, 6]
    assert product_array([3, 2, 1]) == [2, 3, 6]
