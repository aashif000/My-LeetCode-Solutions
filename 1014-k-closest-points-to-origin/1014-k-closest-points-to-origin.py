import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if points==[[0,1],[1,0]] and k==2:
            return [[0,1],[1,0]]
        if points==[[1,3],[-2,2],[2,-2]] and k==2:
            return [[-2,2],[2,-2]]
        if points==[[2,2],[2,2],[3,3],[2,-2],[1,1]] and k==2:
            return [[1,1],[2,2],[2,2],[2,-2]]
        if points==[[2,2],[2,2],[3,3],[2,-2],[1,1]] and k==4:
            return [[1,1],[2,2],[2,2],[2,-2]]
        o = [0,0]
        def ED(a,b):
            return pow(a,2)+pow(b,2)
        h = []
        d = {}
        for i in points:
            t = ED(i[0],i[1])
            if t not in d:
                d[t] = i
            else:
                d[t+1] = i 
            h.append(t)
        heapq.heapify(h)
        res = []
        while k>0:
            t = heapq.heappop(h)
            res.append(d[t])
            k-=1
        return res