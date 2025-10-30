from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        def buildTree(tree, i):
            l = i * 2 + 1
            r = i * 2 + 2
            min_idx = i
            if l < k and tree[l][1] < tree[min_idx][1]:
                min_idx = l
            if r < k and tree[r][1] < tree[min_idx][1]:
                min_idx = r
            if i != min_idx:
                tmp = tree[i]
                tree[i] = tree[min_idx]
                tree[min_idx] = tmp
                buildTree(tree, min_idx)
        num2cnt = dict()
        for num in nums:
            if num in num2cnt:
                num2cnt[num] += 1
            else:
                num2cnt[num] = 1
        tree = [(-1, 0)] * k
        for num, cnt in num2cnt.items():
            if cnt > tree[0][1]:
                tree[0] = (num, cnt)
                buildTree(tree, 0)
        return [x[0] for x in tree]
    

print(Solution().topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))