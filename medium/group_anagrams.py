# Sorted
def sort_group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams = {}
    for i in range(len(strs)):
        sorted_word = "".join(sorted(strs[i]))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [strs[i]]
        else:
            anagrams[sorted_word].append(strs[i])
    return list(anagrams.values())


# Time Complexity: T(n) x T(k log k) + T(1) + T(n). I think if we set the longest word length possible to k, the time complexity becomes O(nk log k) because we sort a word in each iteration and each word sort costs T(k log k) at worst


# Count
def count_group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams = {}
    for i in range(len(strs)):
        word_key = {}
        for word in strs[i]:
            word_key[word] = word_key.get(word, 0) + 1
        word_key = frozenset(word_key.items())
        anagrams.setdefault(word_key, []).append(strs[i])
    return list(anagrams.values())


# Time Complexity: T(n) x T(k) + T(k) + T(1) + T(1) = O(n x k). This is faster.


def main():
    print(sort_group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(count_group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == "__main__":
    main()
