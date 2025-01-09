#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        x = max(arr)
        if k == len(arr):
            return x
        kk = [0] * (x+1)
        for i in arr:
            kk[i] += 1
        for i in range(x):
            if kk[i] > 0:
                k -= kk[i]
            if k <= 0:
                return i
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))
        print("~")
# } Driver Code Ends