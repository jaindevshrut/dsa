class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        x,y = set(),set()
        if A[0] == B[0]:
            ans.append(1)
        else:
            ans.append(0)
            x.add(A[0])
            y.add(B[0])
        for i in range(1,len(A)):
            if A[i] == B[i]:
                ans.append(ans[-1]+1)
            else:
                x.add(A[i])
                y.add(B[i])
                t = x.intersection(y)
                x -= t
                y -= t
                ans.append(ans[-1]+len(t))
        return ans
