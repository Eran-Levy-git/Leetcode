from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            wealth = sum(customer)
            max_wealth = max(max_wealth, wealth)
        return max_wealth

"""
accounts = [[1, 5], [7, 3], [2, 8]]
Customer 0 has wealth: 1 + 5 = 6
Customer 1 has wealth: 7 + 3 = 10
Customer 2 has wealth: 2 + 8 = 10
Both Customer 1 and Customer 2 have the same maximum wealth of 10

accounts = [[10]]
There is only one customer with wealth 10

accounts = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
All customers have zero wealth
The richest customer has wealth 0

"""

# Test Cases
test_cases = [
    [[1, 5], [7, 3], [2, 8]],
    [[10]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
]

sol = Solution()

for i, accounts in enumerate(test_cases):
    result = sol.maximumWealth(accounts)
    print(f"Test Case {i+1}: {result}")