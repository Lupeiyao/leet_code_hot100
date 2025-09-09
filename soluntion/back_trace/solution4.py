from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        def help(start: int, target: int) -> List[List[int]]:
            result = []
            if start >= size:
                return result
            # 选择当前数字，那么结果
            if target == candidates[start]:
                result.append([candidates[start]])
            if target > candidates[start]:
                tmp = help(start, target - candidates[start])
                for x in tmp:
                    x.append(candidates[start])
                result.extend(tmp)
            result.extend(help(start + 1, target))
            return result
        return help(0, target)
    
print(Solution().combinationSum([12,7], 7))