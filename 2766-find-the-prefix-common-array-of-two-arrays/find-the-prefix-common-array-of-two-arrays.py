class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # frequency wala badiya h usme A,B dono permutations h toh hame track rahege numbers ke if kisi ki freq 2 ho gyi mtlb vo dno me aa gaya h
        ans = []
        freq = [0]*(len(A)+1)
        curr = 0
        for i in range(len(A)):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                curr += 1
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                curr += 1
            ans.append(curr)
        return ans