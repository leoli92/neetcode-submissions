class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        current_sum = 0
        ans = []
        left = 0
        right = len(numbers) - 1
        while True:
                if numbers[left] + numbers[right] > target:
                    right -= 1
                elif numbers[left] + numbers[right] < target:
                    left += 1
                else:
                    ans.append(left+1)
                    ans.append(right+1)
                    return ans




        