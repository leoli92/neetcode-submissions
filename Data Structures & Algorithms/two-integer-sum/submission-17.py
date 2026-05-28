class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap idea
        #if target - nums is arleady in dictionary then we have found our pair
        #method is also using get in dicitonaries
        hashmap = {}
#actually no need for the list at all because we can find the PAIR when we
#find the current index that's paired so we can identify the other half
#in the dictionary
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return[hashmap[target-num], i]
            hashmap[num] = i
            
    
    
