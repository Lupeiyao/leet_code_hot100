from typing import List 


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        # 记录每个字母的第一次和最后一次出现下标
        char2Idx = dict()
        for i in range(len(s)):
            if s[i] in char2Idx:
                char2Idx[s[i]][1] = i
            else:
                char2Idx[s[i]] = [i, i]
        i = 0
        while i < len(s):
            end = char2Idx[s[i]][1]
            start = i + 1
            while start < end:
                ch = s[start]
                end = max(end, char2Idx[ch][1])
                start += 1
            result.append(end - i)
            i = end + 1
        return result
    

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))

        
