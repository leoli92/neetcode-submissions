class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        comp = ''
        s1freq = {}
        compfreq = {}
        for eles in s1:
            s1freq[eles] = s1freq.get(eles, 0) + 1

        for right in range(len(s2) + 1):
            comp = s2[left:right]
            while len(comp) == len(s1):
                for ele in comp:
                    compfreq[ele] = compfreq.get(ele, 0) + 1

                if s1freq == compfreq:
                    return True
                else:
                    left+=1
                    comp = s2[left:right]
                    compfreq.clear()
                
        return False
            


