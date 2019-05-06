def cons(a, b):
    """
    cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first
    and last element of that pair. For example, car(cons(3, 4)) returns 3,
    and cdr(cons(3, 4)) returns 4.

    Given this implementation of cons – implement car and cdr.
    """
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    return pair(lambda a, b: a)

    # def func(a, b):
    #     return a
    # return pair(func)


def cdr(pair):
    return pair(lambda a, b: b)

    # def func(a, b):
    #     return b
    # return pair(func)


if __name__ == '__main__':
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4
