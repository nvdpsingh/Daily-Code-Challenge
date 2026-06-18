class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        num = 0
        l,r = 0, x//2
        while l<=r:
            mid = (l+r)//2
            if mid*mid == x:
                return mid
            elif mid*mid<x:
                num = mid
                l = mid+1
            else:
                r = mid-1
        return num
                
        