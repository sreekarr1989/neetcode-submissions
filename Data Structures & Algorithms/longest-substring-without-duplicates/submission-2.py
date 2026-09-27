class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        characters = set()
        left = 0
        right = 0
        max_length = 0

        while right < len(s):

            # Keep removing from the left
            # until the duplicate is gone
            while s[right] in characters:
                characters.remove(s[left])
                left += 1

            # Add the current character
            characters.add(s[right])

            # Calculate current window length
            max_length = max(max_length, right - left + 1)

            right += 1

        return max_length

