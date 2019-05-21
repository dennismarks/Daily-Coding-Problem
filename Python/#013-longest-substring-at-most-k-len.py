def longest_substring_at_most_k_len(k, s):
    """
    Given an integer k and a string s, find the length of the longest substring
    that contains at most k distinct characters.

    For example, given s = "abcba" and k = 2, the longest substring with k
    distinct characters is "bcb".
    """
    start_index, end_index, longest_s = 0, 0, ""

    while end_index < len(s):
        end_index += 1
        num_of_uniq = len(set(s[start_index:end_index]))
        if num_of_uniq <= k:
            longest_s = s[start_index:end_index]
        else:
            start_index += 1

    return longest_s


if __name__ == '__main__':
    assert longest_substring_at_most_k_len(2, "abcba") == "bcb"
    assert longest_substring_at_most_k_len(2, "abccba") == "bccb"
    assert longest_substring_at_most_k_len(2, "aabcba") == "aab"
    assert longest_substring_at_most_k_len(2, "babcba") == "bab"
    assert longest_substring_at_most_k_len(3, "abcba") == "abcba"
    assert longest_substring_at_most_k_len(3, "babcba") == "babcba"
