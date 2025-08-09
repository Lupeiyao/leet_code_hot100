from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        pre = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= pre[1]:
                pre[1] = max(pre[1], intervals[i][1])
            else:
                result.append(pre)
                pre = intervals[i]
        result.append(pre)
        return result
    

print(Solution().merge( [[1,3],[2,6],[8,10],[15,18]]))