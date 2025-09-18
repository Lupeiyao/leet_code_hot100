from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        pre_min = prices[0]
        for i in range(1, len(prices)):
            if pre_min < prices[i]:
                result = max(result, prices[i] - pre_min)
            pre_min = min(pre_min, prices[i])
        return result
    

print(Solution().maxProfit([7,1,5,3,6,4]))