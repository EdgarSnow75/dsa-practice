# Problem No. 704

"""
Set the mid value by halfing the length of the nums list
Set a current_list by setting it to num_list
Loop over the num_list as long as mid is not 0
    In each loop, see if mid is the target
        If so, return mid
    If mid is higher than target,
        half the current_list from 0 to mid (left side)
    Elif mid is lower than target,
        half the current_list from mid to len(num_list)
    Half the value of mid using the current_list
"""


# Loop version
def loop_binary_search(num_list: list[int], target: int) -> int:
    # if len(num_list) == 0:
    #     return -1
    # mid = (len(num_list) // 2) - 1
    # current_index = mid
    # current_list = num_list
    # while mid != 0:
    #     if current_list[mid] == target:
    #         return current_index + 1
    #     if current_list[mid] > target:
    #         current_list = current_list[:mid]
    #         mid = len(current_list) // 2
    #         current_index -= mid
    #     elif current_list[mid] < target:
    #         current_list = current_list[mid + 1 :]
    #         mid = len(current_list) // 2
    #         current_index += mid
    # return -1
    low = 0
    high = len(num_list) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if num_list[mid] == target:
            return mid
        if num_list[mid] > target:
            high = mid - 1
        elif num_list[mid] < target:
            low = mid + 1
    return -1


# Recursive
def binary_search(nums: list[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    mid = (len(nums) // 2) - 1
    if nums[mid] == target:
        return mid + 1
    if nums[mid] > target:
        return binary_search(nums[:mid], target)
    elif nums[mid] < target:
        return binary_search(nums[mid + 1 :], target)


def main():
    print(loop_binary_search([-1, 0, 3, 5, 9, 12], 9))
    # print(binary_search([-1, 0, 3, 5, 9, 12], 9))


if __name__ == "__main__":
    main()
