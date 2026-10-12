# Problem No. 1
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         l, r = 0, 1
#         while l < len(nums):
#             while r < len(nums):
#                 if  nums[l] + nums[r] == target:
#                     return [l, r]
#                 r += 1
#             l += 1
#             r = l + 1


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        passed_nums = {}
        for index, value in enumerate(nums):
            if target - value in passed_nums:
                return [passed_nums[target - value], index]
            passed_nums[value] = index


# Time: O(n) because of the loop. The target - value lookup in the passed_nums set is O(1) so the loop is the most demanding cost.
# Space: O(n) because the hash map grows with the number of input
