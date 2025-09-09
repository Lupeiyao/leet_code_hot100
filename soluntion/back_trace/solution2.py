from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = self.help(nums, 0)
        result.append([])
        return result


    def help(self, nums: List[int], idx: int) -> List[List[int]]:
        result = []
        if idx < len(nums):
            sub_res_list = self.help(nums, idx + 1)
            result.append([nums[idx]])
            result.extend(sub_res_list)
            for sub_res in sub_res_list:
                result.append([nums[idx]] + sub_res)
        return result
    
print(Solution().subsets([1,2,3]))