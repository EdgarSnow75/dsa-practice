# LeetCode 268
import time as tm


# Sorted
def sort_missing_number(nums: list[int]) -> int:
    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums)):
        if i != sorted_nums[i]:
            return i
    return len(sorted_nums)


# Time: O(n log n) because of sorting
# Space: O(n)


# Set
def set_missing_number(nums: list[int]) -> int:
    distinct_nums = len(nums)
    nums = set(nums)
    for num in range(distinct_nums):
        if num not in nums:
            return num
    return distinct_nums


# Time: O(n) because of loop
# Space: O(n)


# Arithmetic
def ari_missing_number(nums: list[int]) -> int:
    correct_len = len(nums) + 1
    print(correct_len)
    correct_sum = (correct_len * (correct_len - 1)) / 2
    wrong_sum = 0
    for num in nums:
        wrong_sum += num
    print(correct_sum)
    print(wrong_sum)
    return correct_sum - wrong_sum


# Time: O(n)
# Space: O(1)


def main():
    start_time = tm.perf_counter()
    print(f"Sorted: {sort_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])}")
    end_time = tm.perf_counter()
    print(f"Time taken: {end_time - start_time}s")
    print(start_time)
    print(end_time)

    print("---------------------------------------------")
    start_time = tm.perf_counter()
    print(f"Set: {set_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])}")
    end_time = tm.perf_counter()
    print(f"Time taken: {end_time - start_time}s")
    print(start_time)
    print(end_time)

    print("---------------------------------------------")
    start_time = tm.perf_counter()
    print(f"Arithmetic: {ari_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])}")
    end_time = tm.perf_counter()
    print(f"Time taken: {end_time - start_time}s")
    print(start_time)
    print(end_time)


if __name__ == "__main__":
    main()
