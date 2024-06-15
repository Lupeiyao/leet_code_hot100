from typing import List


class Solution6:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        result = []
        if p_len > s_len:
            return result
        # 用数组来记录每个sub_str的内容
        s_arr, p_arr = [0] * 26, [0] * 26
        for i in range(p_len):
            s_arr[ord(s[i]) - 97] += 1
            p_arr[ord(p[i]) - 97] += 1
        if s_arr == p_arr:
            result.append(0)
        for i in range(1, s_len - p_len + 1):
            s_arr[ord(s[i - 1]) - 97] -= 1
            s_arr[ord(s[i + p_len - 1]) - 97] += 1
            if s_arr == p_arr:
                result.append(i)
        return result



print(Solution6().findAnagrams("cbaebabacd", "abc"))
