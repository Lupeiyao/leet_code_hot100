from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        size = len(s)
        if size <= 1:
            return 0
        dp = [0] * size
        for i in range(1, size):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2 + dp[i - 2] if i - 2 >= 0 else 2
                elif s[i - 1] == ')':
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = dp[i - 1] + 2
                        if i - dp[i - 1] - 2 >= 0:
                            dp[i] += dp[i - dp[i - 1] - 2]
        return max(dp)
    

print(Solution().longestValidParentheses("(()())"))