"""
Given a string s, find the length of the longest substring
that contains no repeating characters.
"""

def longest_substring(s: str):
    start = 0
    end = 1
    seen = set(s[start])
    max_length = 1

    while end < len(s):
        next_character = s[end]
        if next_character in seen:
            while next_character in seen:
                seen.remove(s[start])
                start+=1
        end+=1
        seen.add(next_character)
        max_length = max(max_length, end-start)
    return max_length

### OUTPUT
s = "abcabcbb"
print(longest_substring(s))
# Output: 3  # "abc"

s = "bbbbb"
print(longest_substring(s))
# Output: 1  # "b"

s = "pwwkew"
print(longest_substring(s))
# Output: 3  # "wke"
