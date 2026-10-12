# Problem No. 1480
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        new_nums = []
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            new_nums.append(running_sum)
        return new_nums


# Time: O(n) because of the loop
# Space: O(n) because the memory of new_nums grows with the length of nums. The output does not count.
