class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #binary search
        left = 1
        right = max(piles)

        while left < right:
            k = left + (right - left) // 2
            hours = 0
            for pile in piles:
                hours += (pile + k-1)//k
            
            if hours <= h:
                right = k
            else:
                left = k+1
        return left

        '''
        #Brute force
        max_pile = max(piles)

        #Try every possible speed
        for k in range(1,max_pile):
            total_hours = 0

            for p in piles:
                total_hours += (p + k-1)//k
            if total_hours <= h:
                return k
        
        return max_pile '''
