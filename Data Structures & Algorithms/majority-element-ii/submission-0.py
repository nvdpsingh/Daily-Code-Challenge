class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict1 = {}
        res = []
        for c in nums:
            if c in dict1:
                dict1[c]+=1
            else:
                dict1[c]=1
        for key,value in dict1.items():
            if value>(len(nums)/3):
                res.append(key)
        return res