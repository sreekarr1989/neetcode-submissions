class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxArea = 0
        
        while i < j:
            minHeight = min(heights[i],heights[j])
            currentArea = minHeight * (j - i)
            maxArea = max(maxArea, currentArea)
            
            # Move the pointer with the smaller height
            if(heights[i] < heights[j]):
                i += 1
            else:
                j -=1
            
        
        return maxArea

        