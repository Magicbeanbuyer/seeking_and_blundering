import pytest as pytest


def length_of_longest_string(s: str) -> int:
    start = 0
    char_map = {}
    length = 1
    # a b cdgh b ef b
    for i in range(len(s)):
        char = s[i]
        if char not in char_map.keys():
            char_map[char] = i
            length = i - start + 1
        else:
            start = char_map[char] + 1
            length = max(i - start + 1, length)
            char_map[char] = i
    return length


@pytest.mark.parametrize("string, length", [
    ['aaaa', 1],
    ["abdcb", 4],
    ["abcbqw", 4],
    ["abcabc", 3],
    ["a", 1]
])
def test_length_of_longest_string(string, length):
    assert length_of_longest_string(string) == length


