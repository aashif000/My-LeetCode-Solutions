class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        cal = []
        for i in matrix:
            cal.extend(i)
        cal = sorted(cal)
        return cal[k-1]                