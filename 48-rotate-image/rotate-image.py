class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        res = []
        m = len(matrix[0])
        for i in range(m):
            t = []
            for j in matrix:
                t.append(j[i])
            t = t[::-1]
            res.append(t) 
        matrix[:] = res