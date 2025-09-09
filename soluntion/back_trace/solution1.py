from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.traveled = [0] * len(nums)

        result = self.help(nums)
        return result


    def help(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            if self.traveled[i] == 0:
                self.traveled[i] = 1
                sub_res_list = self.help(nums)
            
                for sub_res in sub_res_list:
                    sub_res.insert(0, nums[i])
                if len(sub_res_list) == 0:
                    result.append([nums[i]])
                else:
                    result.extend(sub_res_list)
                self.traveled[i] = 0
        return result
    
print(Solution().permute([1,2,3]))