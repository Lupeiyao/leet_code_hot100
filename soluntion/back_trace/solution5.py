from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        if n == 2:
            return ['()()', '(())']
        result = []
        for i in range(n):
            left = self.generateParenthesis(i)
            right = self.generateParenthesis(n - i - 1)
            for x in left:
                for y in right:
                    result.append(f'({x}){y}')
        return result
    

print(Solution().generateParenthesis(3))