class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            if 1 <= int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]

            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n] 
        