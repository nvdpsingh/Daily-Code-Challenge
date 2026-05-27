class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key = lambda x:x[0])
        i,j = intervals[0][0],intervals[0][1]
        for start,end in intervals[1:]:
            if (start,end) == (i,j):
                count+=1
                continue
            #if start<j<end or i<end<j:
            if start<j:
                count+=1
                if end<j:
                    i,j = start,end
            else:
                i,j = start,end
        return count

        