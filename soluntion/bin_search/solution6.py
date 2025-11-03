from typing import List 


class Solution:

    def help(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2
        nums1_len = m // 2
        while nums1_len >= 0 and nums1_len <= m:
            nums2_len = half_len - nums1_len
            nums1_left_max = -10E8 if nums1_len == 0 else nums1[nums1_len - 1]
            nums2_left_max = -10E8 if nums2_len == 0 else nums2[nums2_len - 1]
            nums1_right_min = 10E8 if nums1_len == m else nums1[nums1_len]
            nums2_right_min = 10E8 if nums2_len == n else nums2[nums2_len]
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if (m + n) % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
            elif nums1_left_max > nums2_right_min:
                nums1_len -= 1
            else:
                nums1_len += 1
        return 0
    

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m <= n:
            return self.help(nums1, nums2)
        else:
            return self.help(nums2, nums1)
        

print(Solution().findMedianSortedArrays([1,2], [3]))