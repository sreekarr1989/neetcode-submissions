class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s))+"#"+s)
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i< len(s):
            #find # that separates length from the string
            j = i
            while s[j] != '#':
                j += 1
            
            # Convert the characters before '#' into an integer
            length = int(s[i:j])

            #start of actual string
            start = j+1
            end  = start + length
            newString = s[start:end]
            output.append(newString)

            #Move i to the beginning of the next encoded string
            i = end
        
        return output

