from typing import List


class Solution1:
    def trap(self, height: List[int]) -> int:
        if height is None or len(height) < 3:
            return 0
        result = 0
        left_max, right_max = [0], [0]
        for i in range(1, len(height)):
            left_max.append(max(left_max[-1], height[i - 1]))
        for i in range(len(height) - 2, -1, -1):
            right_max.insert(0, max(right_max[0], height[i + 1]))
        for i in range(1, len(height)):
            result += max(0, min(left_max[i], right_max[i]) - height[i])
        return result


s1 = Solution1()
print(s1.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


