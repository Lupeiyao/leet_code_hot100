from typing import List 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = [0] + [-1] * amount
        for num in range(1, amount + 1):
            num_result = float('inf')
            for coin in coins:
                if num >= coin and result[num - coin] != -1:
                    num_result = min(num_result, result[num - coin] + 1)
                    result[num] = num_result
        return result[amount]

print(Solution().coinChange([2], 3))