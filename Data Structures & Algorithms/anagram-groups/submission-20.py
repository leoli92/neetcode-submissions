class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #individual anagrams are done using frequency maps
        ## idea 1: create a frequency map for the first str - then
        ## compare from this index forward if the word fits in this
        ## freq map. 
        ## compare how?? 

        ## thisdict = {
            # "c": 1,
            # "a": 1,
            # "t": 1
            # }
        ## loop through  - comapre character by character
        dic = {}
        current = ''
        ans = []

        for word in strs:
            key = tuple(sorted(word))
            if key not in dic:
                dic[key] = []
            dic[key].append(word)
        
        for item in dic:
            ans.append(dic[item])
            
        return ans
            ## tuples of the sorted word can be the key












            
