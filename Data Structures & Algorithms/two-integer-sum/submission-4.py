class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        
        for i in range (0,len(nums)):
            reminder = target - nums[i]
            if reminder in my_map:
                secondIdx = my_map.get(reminder)
                return [secondIdx, i]
            else:
                my_map[nums[i]] = i
        
        return []
        