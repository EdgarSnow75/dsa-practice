# LeetCode 205
"""
We should set up an dictionary first to track what letter has been replaced with what.
Loop over s
For each iteration,
        Check if the current word of s is in the dict
                if s is not in dict,
                        Check if the t word is already in the dict's values:
                                if so, return False
                        If not, add the s word to the dict with t word as the value
                if s is in dict,
                        check if t word is equal to the value of s word in dict
                                if not, return False
        return True
"""


def is_isomorphic(s: str, t: str) -> bool:
    tracked_words = {}
    for i in range(len(s)):
        if s[i] not in tracked_words:
            if t[i] in tracked_words.values():
                return False
            tracked_words[s[i]] = t[i]
        elif s[i] in tracked_words and tracked_words[s[i]] != t[i]:
            return False
    return True
