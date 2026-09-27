class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #sort
        #[-4,-1,-1,0,1,2]
        nums.sort()
        output = []

        for i in range(len(nums)):

            #skip duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue
            self.twoSum(i,nums, output)
        
        return output
    
    def twoSum(self, i: int, nums: List[int], output: List[List[int]]):
        j = i+1
        k = len(nums)-1

        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                output.append([nums[i],nums[j],nums[k]])
                j += 1
                k -= 1

                #skip duplicate j values
                while j < k and nums[j] == nums[j-1]:
                    j+=1
                
                #skip duplicate k values
                while j < k and nums[k] == nums[k+1]:
                    k-=1

            if sum < 0:
                #need a larger number
                j += 1
            if sum > 0:
                #need a smaller number
                k -= 1 

