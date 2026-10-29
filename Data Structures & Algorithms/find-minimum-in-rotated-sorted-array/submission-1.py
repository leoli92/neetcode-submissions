class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ans = max(nums)
        if nums[left] <= nums[right]:
                return nums[left]
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] <= nums[right]:
                ans = min(ans, nums[mid])
                right = mid - 1
            elif nums[mid] >= nums[left]:
                ans = min(ans, nums[left])
                left = mid + 1
        return ans
                
