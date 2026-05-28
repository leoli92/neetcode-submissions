class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr = ''
        for ch in strs:
            k = len(ch)
            newstr += f'{k}' + '#' + ch
        return newstr

    def decode(self, s: str) -> List[str]:
        i=0
        k=0
        ans = []
        word = ''
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            k = int(s[i:j])
            word = s[j+1 : j+1+k]
            ans.append(word)
            i = j+k+1
        return ans
                




