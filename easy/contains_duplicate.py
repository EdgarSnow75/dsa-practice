# Problem No. 217
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # num_list = {}
        # for num in nums:
        #     if num_list.get(num, 0) == 1:
        #         return True
        #     else:
        #         num_list[num] = 1
        # return False
        # Time: O(n) because of the loop.
        # Space: O(n) the number of key value pairs in the num_list grows with the number of input

        # Nested loop solution
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        # Time: O(n^2) because of the nested loop
        # Space: O(1) memory used does not grow with the size of the input

        # Sort-first
        sorted_nums = sorted(nums)
        for i in range(len(nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                return True
        return False
        # Time: O(n log n) because of sorted is n log n. The loop for i in range adds O(n) but since O(2n log n) is still counted as O(n log n)

        # Space: O(n) because the memory grows with the input size
