class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for ch in logs:
            if ch=='../' and count>=0:
                count = (count-1) if count>0 else 0
            elif ch=='./':
                continue
            else:
                count+=1
        return count