class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        balloons = points
        
        if not balloons:
            return 0
        
        arrows = 1
        balloons.sort()
        previous_end = balloons[0][1]
        for start,end in balloons[1:]:
            if start > previous_end:
                arrows += 1
                previous_end = end
            else:
                previous_end = min(previous_end,end)

            
        return arrows