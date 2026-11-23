# LeetCode 290
def word_pattern(pattern: str, s: str) -> bool:
    splitted_words = s.split()
    if len(pattern) != len(splitted_words):
        return False
    tracked_pattern = {}
    for i in range(len(pattern)):
        if pattern[i] not in tracked_pattern:
            if splitted_words[i] in tracked_pattern.values():
                return False
            tracked_pattern[pattern[i]] = splitted_words[i]
        elif (
            pattern[i] in tracked_pattern
            and tracked_pattern[pattern[i]] != splitted_words[i]
        ):
            return False
    return True
