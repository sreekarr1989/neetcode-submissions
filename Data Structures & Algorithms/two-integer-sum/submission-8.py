class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_map = {}
        for i in range(len(nums)):
            reminder = target - nums[i]
            if reminder in my_map:
                return [my_map[reminder],i]
            else:
                my_map[nums[i]] = i
        return []


        