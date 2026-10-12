# Problem No. 2778
class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        nums_len = len(nums)
        squared_sum = 0
        for i in range(nums_len):
            if nums_len % (i + 1) == 0:
                squared_sum += nums[i] * nums[i]
        return squared_sum


# Time: O(n) due to the loop. The steps grow with the length of the input.
# Space: O(1) the memory space does not grow with the input
