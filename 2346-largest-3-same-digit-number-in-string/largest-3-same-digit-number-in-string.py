class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = []
        def slide(s):
            nonlocal res
            k = 3
            n = len(s)
            for i in range(n):
                t = s[i:i+k]
                if len(t)<3:
                    continue
                elif len(set(t))==1:
                    res.append(t)
        slide(num)
        res.sort()
        return res[-1] if res else ""