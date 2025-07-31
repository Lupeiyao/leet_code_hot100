from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        char_diff = [0] * 26
        for i in range(0, len(s) - len(p) + 1):
            if i == 0:
                for j in range(len(p)):
                    char_diff[ord(s[j]) - 97] += 1
                    char_diff[ord(p[j]) - 97] -= 1
            else:
                char_diff[ord(s[i - 1]) - 97] -= 1
                char_diff[ord(s[i + len(p) - 1]) - 97] += 1
            if len([x for x in char_diff if x != 0]) == 0:
                result.append(i)
        return result
            
print(Solution().findAnagrams("cbaebabacd", "abc"))