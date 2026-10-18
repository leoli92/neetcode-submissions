class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        else:
            tfreq = {}
            for c in t:
                tfreq[c] = tfreq.get(c, 0) + 1
            sfreq = {}
            left = 0
            right = len(t) - 1
            best_length = float("inf")
            have = 0
            need = len(tfreq)
            for right in range(len(s)):
                sfreq[s[right]] = sfreq.get(s[right], 0) + 1
                if s[right] in tfreq and sfreq[s[right]] == tfreq[s[right]]:
                    have += 1
                
                while have == need:
                    if right - left + 1 < best_length:
                        best_length = right - left + 1
                        best = (left, right)

                    sfreq[s[left]] -= 1

                    if s[left] in tfreq and sfreq[s[left]] < tfreq[s[left]]:
                        have -= 1
                    left+=1

        if best_length == float("inf"):
            return ""

        l, r = best
        return s[l: r+1]
            


                    


