class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i] = 1
        res = []
        sh = {k:v for k,v in  sorted(h.items(),key=lambda item:item[1],reverse=True)}
        print(sh)
        j = 0
        for i in sh:
            if j==k:
                break
            j+=1
            res.append(i)
        return res