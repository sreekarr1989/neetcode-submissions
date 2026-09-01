class Solution:
    #time complexity:O(n log n) + O(n log n) + O(n) = O(n log n)
    #space complexity: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = sorted(s) #returns list of characters
        t = sorted(t)

        i = 0
        while i < len(s):
            if s[i] != t[i]:
                return False
            i += 1

        return True

        #approach 2:
        #time: O(n+m)
        #space: O(1)
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] +=1
            count[ord(t[i]) - ord('a')] -=1
        
        for val in count:
            if val !=0:
                return False
        return True
            