from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_to_group = {}
        for str in strs:
            tmp = "".join(sorted(str))
            if tmp in str_to_group:
                str_to_group[tmp].append(str)
            else:
                str_to_group[tmp] = [str]
        return list(str_to_group.values())