from typing import List


class Solution3:

    def minWindow(self, s: str, t: str) -> str:
        result = ""
        # map记录每个字符出现的次数
        ch_to_cnt = dict()
        for ch in t:
            if ch in ch_to_cnt:
                ch_to_cnt[ch] += 1
            else:
                ch_to_cnt[ch] = 1
        start = 0
        # 滑窗一直向右
        for i in range(len(s)):
            if s[i] not in ch_to_cnt:
                continue
            ch_to_cnt[s[i]] -= 1
            if ch_to_cnt[s[i]] > 0 or not func(ch_to_cnt):
                continue
            # 如果新加入的字符使得s[start: i + 1]满足条件，则收缩左边
            while start <= i:
                if s[start] not in ch_to_cnt:
                    start += 1
                elif ch_to_cnt[s[start]] < 0:
                    ch_to_cnt[s[start]] += 1
                    start += 1
                else:
                    break
            if result == "" or i - start + 1 < len(result):
                result = s[start: i + 1]
        return result


def func(ch_to_cnt):
    for val in ch_to_cnt.values():
        if val > 0:
            return False
    return True




print(Solution3().minWindow("minWindowADOBECODEBANC", "ABC"))
