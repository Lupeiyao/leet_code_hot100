from typing import List

class Solution:

    def __init__(self):
        self.str_to_result = dict()
        self.str_to_result[''] = [[]]
        

    def partition(self, s: str) -> List[List[str]]:
        if s in self.str_to_result:
            return self.str_to_result[s]
        size = len(s)
        result = []
        if size == 1:
            result.append([s])
            self.str_to_result[s] = result
            return result
        
        # 从任何位置都可分割
        for i in range(1, size + 1):
            sub_str = s[0: i]
            # 分割位置左边是回文串，获取右边的分割结果然后合并
            if sub_str == sub_str[-1::-1]:
                sub_result = self.partition(s[i:])
                for tmp in sub_result:
                    result.append([sub_str] + tmp)
        self.str_to_result[s] = result
        return result
    

print(Solution().partition("aab"))