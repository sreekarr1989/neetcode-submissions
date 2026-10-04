class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}

        for s in strs:
            sortedString = "".join(sorted(s)) #new string
            if sortedString in my_map:
                #append
                my_map[sortedString].append(s)
            else:
                my_map[sortedString] = [s]
        
        return list(my_map.values())