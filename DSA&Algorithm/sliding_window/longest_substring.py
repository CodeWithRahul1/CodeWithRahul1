def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


s = "abcabcbb"
print(length_of_longest_substring(s))

def longest_substring(s: str):
    char_set = set()
    left = 0
    max_len = 0
    start_idx = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])

        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_idx = left

    return s[start_idx:start_idx + max_len]


# Example usage
s = "abcabcbb"
print(longest_substring(s))  # Output: "abc"
