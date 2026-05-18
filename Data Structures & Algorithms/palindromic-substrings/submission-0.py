class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        l,r = 0,0
        for i in range(n):
            l=r= i
            for j in range(i,n):
                if l>=0 and r<=n-1 and s[l]==s[r]:
                    res+=1
                    l-=1
                    r+=1
                else:
                    break
            l=i
            r=i+1
            for j in range(i,n):
                if l>=0 and r<=n-1 and s[l]==s[r]:
                    res+=1
                    l-=1
                    r+=1
                else:
                    break
        return res