from typing import List


class Solution5:
    """给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。"""
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        result, start, char_set = 1, 0, {s[0]}
        # 以s[end]为结尾的最长字串
        for end in range(1, len(s)):
            while start < end and s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            result = max(result, end - start + 1)
        return result






