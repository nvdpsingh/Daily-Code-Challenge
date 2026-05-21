class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmin = currmax = ans  = nums[0]

        for n in nums[1:]:
            if n<0:
                currmax , currmin = currmin, currmax
            currmax = max(n,currmax*n)
            currmin = min(n,currmin*n) 

            ans = max(ans,currmax)
        return ans

        