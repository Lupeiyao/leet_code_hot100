from typing import List
import collections


class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_to_group = collections.defaultdict(list)
        for str in strs:
            tmp = "".join(sorted(str))
            str_to_group[tmp].append(str)
        return list(str_to_group.values())


