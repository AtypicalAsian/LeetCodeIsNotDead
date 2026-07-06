class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # [x,y] - interval
        #sort by ascending x, descending y so that e.g 1,4 in front of 1,2 -> helps
        # when we check i+1 interval against ith interval
        
        intervals.sort(key=lambda x: (x[0], -x[1])) #sorting takes care of the x0 value -> the x value of i+1 interval will always be >= the x value of the ith interval
        # print(intervals)

        count = 0
        prev_end = -1
        for start,end in intervals:
            # curr_end > largest previous end -> curr interval is not covered
            if end > prev_end:
                count += 1
                prev_end = end
            #else, this interval is already covered
        return count