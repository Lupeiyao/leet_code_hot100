from typing import List


class Solution7:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_to_count = {0: 1}
        sum_val, result = 0, 0
        for i in range(len(nums)):
            sum_val += nums[i]
            if sum_val - k in sum_to_count:
                result += sum_to_count[sum_val - k]
            if sum_val in sum_to_count:
                sum_to_count[sum_val] += 1
            else:
                sum_to_count[sum_val] = 1
        return result

print(Solution7().subarraySum([1,1,1], 2))