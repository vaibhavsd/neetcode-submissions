class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        maxsum= 0
        sliddict= defaultdict(int)
        start= 0
        end= 0
        while True:
            if start== len(s):
                break

            sliddict[s[start]]+=1
            totalsum= sum(sliddict.values())
            maxfreq= max(sliddict.values())     
            if totalsum-maxfreq>k:
                sliddict[s[end]]-=1
                end+=1
            else:
                maxsum= max(maxsum, totalsum)
            start+=1
        return maxsum
