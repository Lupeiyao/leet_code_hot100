class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        result = 0
        char_set = set()
        right = -1
        str_size = len(s)
        for (idx, ch) in enumerate(s):
            if idx != 0:
                char_set.remove(s[idx - 1])
            while right + 1 < str_size and s[right + 1] not in char_set:
                char_set.add(s[right + 1])
                right += 1
            result = max(result, right - idx + 1)
        return result
    

print(Solution().lengthOfLongestSubstring("pwwkew"))
