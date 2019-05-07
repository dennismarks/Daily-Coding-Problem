def ways_to_decode(s):
    """
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
    count the number of ways it can be decoded.

    For example, the message '111' would give 3, since it could be decoded
    as 'aaa', 'ka', and 'ak'.

    You can assume that the messages are decodable. For example, '001'
    is not allowed.
    """
    if len(s) == 1:
        return 1
    elif len(s) == 2:
        return 1 + is_valid_code(int(s))
    else:
        count = ways_to_decode(s[1:])
        if is_valid_code(int(s[:2])):
            count += ways_to_decode(s[2:])
    return count


def is_valid_code(s):
    if s > 26 or s < 1:
        return 0
    return 1


if __name__ == '__main__':
    assert ways_to_decode("11") == 2
    assert ways_to_decode("111") == 3
    assert ways_to_decode("1111") == 5
    assert ways_to_decode("1212") == 5

