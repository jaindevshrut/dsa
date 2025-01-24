class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        nodes = [[0,0] for _ in range(n+1)]
        if n == 1:
            return 1
        # [0] jana 
        # [1] aana
        for i,j in trust:
            nodes[i][0] += 1
            nodes[j][1] += 1
        for i in range(n+1):
            if nodes[i][0] == 0 and nodes[i][1] == n - 1:
                return i
        return -1
        