from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        pre_sum = [nums[0]]
        for i in range(1, len(nums)):
            pre_sum.append(nums[i] + pre_sum[i - 1])
        sum_to_num = {0:1}
        for i in range(0, len(nums)):
            if pre_sum[i] - k in sum_to_num:
                result += sum_to_num[pre_sum[i] - k]
            if pre_sum[i] in sum_to_num:
                sum_to_num[pre_sum[i]] += 1
            else:
                sum_to_num[pre_sum[i]] = 1
        return result

    

print(Solution().subarraySum([1,2,3], 3))

            
