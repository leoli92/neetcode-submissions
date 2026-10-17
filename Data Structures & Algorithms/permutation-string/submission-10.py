class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        comp = ''
        s1freq = {}
        compfreq = {}
        if len(s1) > len(s2):
            return False
        for eles in s1:
            s1freq[eles] = s1freq.get(eles, 0) + 1
        for i in range(len(s1)):
            compfreq[s2[i]] = compfreq.get(s2[i], 0) + 1
        if compfreq == s1freq:
            return True

        for right in range(len(s1), len(s2)):
            compfreq[s2[right]] = compfreq.get(s2[right], 0) + 1
            compfreq[s2[left]] -= 1
            if compfreq[s2[left]] == 0:
                del compfreq[s2[left]]
            left+=1
            if s1freq == compfreq:
                return True
                
                
                
        return False
            


