class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key = lambda x:x[0])
        j = intervals[0][1]
        for start,end in intervals[1:]:
            #if start<j<end or i<end<j:
            if start<j:
                count+=1
                if end<j:
                    j = end
            else:
                j = end
        return count

        