class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n,m = len(mat),len(mat[0])
        rows = [0]*(n)
        cols = [0]*(m)
        dic = {}
        for i in range(n):
            for j in range(m):
                dic[mat[i][j]] = [i,j]
        j = -1
        for i in arr:
            j += 1
            rows[(dic[i])[0]] += 1
            if rows[(dic[i])[0]] == m:
                return j
            cols[(dic[i])[1]] += 1
            if cols[(dic[i])[1]] == n:
                return j