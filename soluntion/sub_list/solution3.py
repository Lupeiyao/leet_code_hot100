
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        result_max_len = len(s) + 1
        t_map = dict()
        for ch in t:
            if ch in t_map:
                t_map[ch] += 1
            else:
                t_map[ch] = 1
        start, end = 0, 0
        while end < len(s):
            if s[end] in t_map:
                t_map[s[end]] -= 1
                while s[start] not in t_map or t_map[s[start]] < 0:
                    if s[start] in t_map:
                        t_map[s[start]] += 1
                    start += 1
                if end - start + 1 < result_max_len and len([x for x in t_map.values() if x > 0]) == 0:
                        result = s[start: end + 1]
                        result_max_len = end - start + 1
            end += 1

        return result
    

print(Solution().minWindow("ADOBECODEBANC", "ABC"))

                