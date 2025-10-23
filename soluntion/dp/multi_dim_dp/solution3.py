from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        size = len(s)
        dp = [[0] * size for _ in range(size)]
        for length in range(1, size + 1):
            for start in range(size):
                if length == 1:
                    dp[start][length - 1] = 1
                elif start + length - 1 < size and s[start] == s[start + length - 1]:
                    if length == 2:
                        dp[start][length - 1] = 1
                    else:
                        dp[start][length - 1] = dp[start + 1][length - 2 - 1]
                if dp[start][length - 1] == 1:
                    result = s[start: start + length]
        return result
    
print(Solution().longestPalindrome("aba"))    

