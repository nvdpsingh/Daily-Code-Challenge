class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                continue
            else:
                res = 0
                while s[i] !=" ":
                    res+=1
                    if i==0:
                        return res
                    else:
                        i-=1
                return res

