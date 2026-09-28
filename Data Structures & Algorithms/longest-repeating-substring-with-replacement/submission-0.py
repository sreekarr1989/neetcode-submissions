class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_counts = {}

        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):

            # Add the character at right pointer
            character = s[right]

            if character not in character_counts:
                character_counts[character] = 0

            character_counts[character] += 1

            # Keep track of the most frequent character
            max_frequency = max(
                max_frequency,
                character_counts[character]
            )

            # Length of current window
            window_length = right - left + 1

            # How many characters need to be replaced?
            replacements_needed = window_length - max_frequency

            # If we need more than k replacements,
            # move the left pointer
            while replacements_needed > k:

                # Remove the character at left
                character_counts[s[left]] -= 1

                # Move left pointer
                left += 1

                # Recalculate window length
                window_length = right - left + 1

                # Recalculate replacements needed
                replacements_needed = window_length - max_frequency

            # Current window is valid
            max_length = max(max_length, window_length)

        return max_length