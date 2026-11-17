# LeetCode 383
def canConstruct(ransomNote: str, magazine: str) -> bool:
    m_count = {}
    for word in magazine:
        m_count[word] = m_count.get(word, 0) + 1

    for word in ransomNote:
        if m_count.get(word) == None or m_count.get(word) == 0:
            return False
        m_count[word] -= 1
    return True


# Time: O(n)
# Space: O(n)
