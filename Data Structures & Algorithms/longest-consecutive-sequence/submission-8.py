class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lis = sorted(nums)
        exist = 1
        seq = 1
        if nums == []:
            return 0
        for i in range(1, len(lis)):
            if lis[i] - lis[i-1] == 1:
                seq += 1
                if seq > exist:
                    exist = seq
            elif lis[i] - lis[i-1] == 0:
                continue
            else:
                seq = 1
        return exist

            

