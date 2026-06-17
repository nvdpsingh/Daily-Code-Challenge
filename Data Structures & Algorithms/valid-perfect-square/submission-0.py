class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 0, (num+1)//2
        while l<=r:
            mid = (l+r)//2
            n= mid*mid
            if n == num:
                return True
            else:
                if n > num:
                    r = mid-1
                else:
                    l = mid+1
        return False
    