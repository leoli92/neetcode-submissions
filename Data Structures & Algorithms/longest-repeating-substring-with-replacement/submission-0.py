class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        most_common = 0
        longest_length = 0
        for right in range(len(s)):
            current_char = s[right]
            counts[current_char] = counts.get(current_char, 0) + 1
            most_common = max(most_common, counts[current_char])

            while (right - left + 1) - most_common > k:
                left_char = s[left]
                counts[left_char] -= 1
                left += 1

            current_length = right - left + 1
            longest_length = max(longest_length, current_length)
        
        return longest_length




        


            

