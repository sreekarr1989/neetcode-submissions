class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        result = [0] * n
#1,2,3,4
        left[0] = right[n-1] = 1
        for i in range(1,n):
            left[i] = nums[i-1] * left [i-1]
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        
        for i in range(n):
            result[i] = left[i] * right[i]
        
        return result


       

        