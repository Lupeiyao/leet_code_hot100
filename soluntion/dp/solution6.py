from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [True] + [False] * length
        for i in range(1, length + 1):
            for word in wordDict:
                word_length = len(word)
                if word_length <= i and dp[i - word_length] and word == s[i - word_length: i]:
                    dp[i] = True 
                    break

        return dp[-1]

print(Solution().wordBreak("leetcode", ["leet", "code"]))            