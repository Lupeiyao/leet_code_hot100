from typing import List


class UnionFindSet:
    def __init__(self, nums):
        self.uf_set = {num: num for num in nums}
        self.uf_num = {num: 1 for num in nums}\
    
    def find(self, num):
        while num != self.uf_set[num]:
            num = self.uf_set[num]
        return num
    
    def merge(self, num1, num2):
        root1 = self.find(num1)
        root2 = self.find(num2)
        if root1 != root2:
            if self.uf_num[root2] > self.uf_num[root1]:
                self.uf_set[root1] = root2
                self.uf_num[root2] += self.uf_num[root1]
            else:
                self.uf_set[root2] = root1
                self.uf_num[root1] += self.uf_num[root2]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        # 并查集解法
        # nums = set(nums)
        # uf_set = UnionFindSet(nums)
        # for num in nums:
        #     if num + 1 in nums:
        #         uf_set.merge(num, num + 1)
        # return max(uf_set.uf_num.values())

        # 递归解法
        nums = set(nums)
        max_length= 1
        for num in nums:
            if num - 1 not in nums:
                curr_num = num
                curr_length = 1
                while curr_num + 1 in nums:
                    curr_num += 1
                    curr_length += 1
                max_length = max(max_length, curr_length)
        return max_length
    

print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    
