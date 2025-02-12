class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mapp = {}
        for i in nums:
            t = sum(list(map(int,str(i))))
            if mapp.get(t) == None:
                mapp[t] = []
            mapp[t].append(i)
        ans = -1
        for i in mapp:
            if len(mapp[i]) > 1:
                ans = max(ans,sorted(mapp[i])[-1]+sorted(mapp[i])[-2])
        return ans
            
        