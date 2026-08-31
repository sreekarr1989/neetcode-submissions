class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Approach 1: Sort
        # Time: O(n log n)
        # Space: O(1)*
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False

        # Approach 2: Using set
        # Time: O(n) average
        # Space: O(n)
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False