from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits is None or "" == digits:
            return []

        dig_2_char = {'2': ['a','b','c'], '3': ['d', 'e', 'f'], '4':['g','h','i'], 
                      '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], 
                      '8':['t','u','v'], '9':['w','x','y','z']}
        result = ['']
        for ch in digits:
            tmp_result = []
            for tmp in result:
                for dig_char in dig_2_char[ch]:
                    tmp_result.append(tmp + dig_char)
            result = tmp_result
        return result
    
print(Solution().letterCombinations("23"))
