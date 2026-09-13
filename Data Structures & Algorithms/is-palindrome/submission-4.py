class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for char in s:
            if char.isalnum():
                clean += char.lower()
        # copy = clean[::-1]
        # for i in range(len(clean)):
        #     if copy[i] != clean[i]:
        #         return False
        # return True
        left = 0
        right = len(clean)-1
        while left < right:
            if clean[left] == clean[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
    


