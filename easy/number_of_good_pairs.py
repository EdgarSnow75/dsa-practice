# Problem No. 1512
class Solution:
    # def num_identical_pairs(self, nums: list[int]) -> int:
    #     num_of_good_pairs = 0
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 num_of_good_pairs += 1
    #     return num_of_good_pairs
    # Time: O(n^2) even though the inner loop decreases in total runs after each iteration of outer loop
    # Space: O(1) since the memory does not grow with the input length

    def num_identical_pairs(self, nums: list[int]) -> int:
        nums_dict = {}
        count_of_pair = 0
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                count_of_pair += nums_dict[
                    nums[i]
                ]  # This is beacuse every added identical value can have multiple new pairings
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1
        return count_of_pair

    # Time: O(n) the steps only grows with the i in range loop. The index lookup using the dict as a hashmap is O(1)
    # Space: O(n) the nums_dict grows with the input size
