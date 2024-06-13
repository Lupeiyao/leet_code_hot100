from typing import List


class UnionFindSet(object):
    def __init__(self, nums):
        self.uf_set = {num: num for num in nums}
        self.uf_num = {num: 1 for num in nums}

    def find(self, idx):
        while idx != self.uf_set[idx]:
            idx = self.uf_set[idx]
        return idx

    def merge(self, num1, num2):
        root1 = self.find(num1)
        root2 = self.find(num2)
        if root1 != root2:
            self.uf_set[root1] = root2
            self.uf_num[root2] += self.uf_num[root1]


class Solution2(object):
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        nums = set(nums)
        uf_set = UnionFindSet(nums)
        for num in nums:
            if num + 1 in nums:
                uf_set.merge(num, num + 1)
        return max(uf_set.uf_num.values())


