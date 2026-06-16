class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 0,n
        if n in [1,2]:
            return 1
        while l<=r:
            mid = (l+r)//2
            if (mid*(mid+1))/2 == n:
                return mid
            elif ((mid*(mid+1))/2)<n:
                l=mid+1
            else:
                r=mid-1
        return r

            


                