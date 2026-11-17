# LeetCode 706
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        hash_buc = self.map[key % self.size]
        for index, (k, _) in enumerate(hash_buc):
            if k == key:
                hash_buc[index] = [key, value]
                return
        hash_buc.append([key, value])

    def get(self, key: int) -> int:
        hash_buc = self.map[key % self.size]
        for _, (k, v) in enumerate(hash_buc):
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        hash_buc = self.map[key % self.size]
        for index, (k, _) in enumerate(hash_buc):
            if k == key:
                hash_buc.pop(index)
                return


# Time: O(1)
# Space: O(n)
