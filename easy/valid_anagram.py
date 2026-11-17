# LeetCode 242
import collections


# Sorted
def valid_anagram_sorted(s: str, t: str) -> bool:
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_t == sorted_s


# Time is O(n log n) because of sorting
# Space O(n) space grows with both input sizes


# Counts
def valid_anagram_count(s: str, t: str) -> bool:
    s_count = {}
    t_count = {}
    for word in s:
        s_count[word] = s_count.get(word, 0) + 1
    for word in t:
        t_count[word] = t_count.get(word, 0) + 1
    return s_count == t_count


# Time is O(n)
# Space is O(n)
# I would pick the cheaper operation of counts over sorted if there are long strings


# Counter
def valid_anagram_counter(s: str, t: str) -> bool:
    return collections.Counter(s) == collections.Counter(t)


def main():
    print(valid_anagram_count("anagram", "nagaram"))
    print(valid_anagram_sorted("anagram", "nagaram"))
    print(valid_anagram_count("rat", "cat"))
    print(valid_anagram_sorted("rat", "cat"))
    print(valid_anagram_counter("anagram", "nagaram"))
    print(valid_anagram_counter("rat", "cat"))


if __name__ == "__main__":
    main()
