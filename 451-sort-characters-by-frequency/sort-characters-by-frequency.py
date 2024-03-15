class Solution:
    def frequencySort(self, s: str) -> str:
        h = {}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i] = 1
        sh = {k: v for k, v in sorted(h.items(), key=lambda item: item[1], reverse=True)}
        res = ""
        for i in sh:
            res+=i*sh[i]
        return res
        