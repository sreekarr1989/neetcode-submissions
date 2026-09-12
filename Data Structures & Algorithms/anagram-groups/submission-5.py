class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            sortedString = sorted(s) #returns new sorted string
            newStr = "".join(sortedString)
            if newStr in hashmap:
                hashmap[newStr].append(s)
            else:
                hashmap[newStr] = [s]#add new list
        
        return list(hashmap.values())