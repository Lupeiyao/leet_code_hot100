from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        if strs == None or len(strs) == 0:
            return result
        str_to_group = {}
        for str in strs:
            tmp = "".join(sorted(str))
            if tmp in str_to_group:
                str_to_group[tmp].append(str)
            else:
                str_to_group[tmp] = [str]
                result.append(str_to_group[tmp])
        return result