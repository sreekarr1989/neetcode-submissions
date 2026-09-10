class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(strs)):
            sortedString = str(sorted(strs[i]))
            if sortedString in hashmap:
                hashmap[sortedString].append(strs[i])
            else:
                hashmap[sortedString] = [strs[i]]
        
        return list(hashmap.values())