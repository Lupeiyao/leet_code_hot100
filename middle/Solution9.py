from typing import List

class Solution9:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按照开始排序，挨个融合即可
        intervals = sorted(intervals, key=lambda x: x[0])
        cur_range = intervals[0]
        result = [cur_range]
        for range in intervals[1:]:
            if range[0] <= cur_range[1]:
                cur_range[1] =max(range[1], cur_range[1])
            else:
                cur_range = range
                result.append(cur_range)
        return result


print(Solution().merge([[1,3],[1,5],[0,10],[15,18]]))