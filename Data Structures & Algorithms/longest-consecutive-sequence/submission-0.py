class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestLength = 0
        for num in nums:
            #Check if its start of sequence.
            #previous number should not be in set
            if (num - 1) not in numSet:
                currentLength = 0
                #check if next number is in set
                while (num + currentLength) in numSet:
                    currentLength +=1
                longestLength = max (longestLength, currentLength)
        return longestLength
        