# Problem No. 35
def search_insert_position(nums: list[str], target: int) -> int:
    low = 0
    high = len(nums)
    while low <= high:
        mid = low + (high - low) // 2
        if mid == high or nums[mid] == target:
            return mid
        if nums[mid] > target:
            high = mid
        elif nums[mid] < target:
            low = mid + 1
    return mid


def main():
    print(search_insert_position([1, 3, 5, 6], 2))
    print(search_insert_position([1, 3, 5, 6], 7))
    print(search_insert_position([1, 3, 5, 6], 5))
    print(search_insert_position([1, 3], 2))
    print(search_insert_position([1, 3, 5, 6], 0))


if __name__ == "__main__":
    main()
