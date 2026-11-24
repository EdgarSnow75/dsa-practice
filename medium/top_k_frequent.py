# LeetCode 347

# Sorted
def top_k_frequent_sorted(nums: list[int], k: int) -> list[int]:
    element_counts = {}
    for i in range(len(nums)):
        element_counts[nums[i]] = element_counts.setdefault(nums[i], 0) + 1
    element_counts = sorted(element_counts, key=element_counts.get, reverse=True)
    return element_counts[:k]


# Buckets
def top_k_frequent_buckets(nums: list[int], k: int) -> list[int]:
    buckets = [[] for _ in range(len(nums) + 1)]
    element_counts = {}
    for i in range(len(nums)):
        element_counts[nums[i]] = element_counts.setdefault(nums[i], 0) + 1

    for index, (key, value) in enumerate(element_counts.items()):
        buckets[value].append(key)
    result = []
    for count in range(len(buckets) - 1, 0, -1):
        for value in buckets[count]:
            result.append(value)
            if len(result) == k:
                return result
