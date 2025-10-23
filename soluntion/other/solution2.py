from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_to_cnt = dict()
        max_cnt = 0
        result = nums[0]
        for num in nums:
            if num in num_to_cnt:
                num_to_cnt[num] += 1
            else:
                num_to_cnt[num] = 1
            if num_to_cnt[num] > max_cnt:
                max_cnt = num_to_cnt[num]
                result = num
        return result

print(Solution().majorityElement([2,2,1,1,1,2,2]))