# Problem No. 1672
class Solution:
    def maximum_wealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            current_wealth = 0
            for j in range(len(accounts[i])):
                current_wealth += accounts[i][j]
            max_wealth = max(max_wealth, current_wealth)
        return max_wealth


# Time: O(r x c) where r is the customers and c is the banks due to the row and column structure of the list and the need to go through each column of each row
# Space: O(1) since we only use two new variables and the memory usage does not grow with the length of input
