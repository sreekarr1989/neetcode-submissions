class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        character_count = {}
        for char in s:
            character_count[char] = character_count.get(char,0)+1
        
        for char in t:
            if char not in character_count:
                return False
            
            character_count[char] -= 1

            if character_count[char] < 0:
                return False
        
        return True

