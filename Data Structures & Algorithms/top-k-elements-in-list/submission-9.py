class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        ans = []
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        descending = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        i = 0
        for num in descending:
            if i >= k:
                return ans
            ans.append(num)
            i+=1
        return ans

        