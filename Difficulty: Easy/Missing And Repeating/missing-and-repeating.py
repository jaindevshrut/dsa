#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        s = set()
        repeat = 0
        sum = 0
        n = len(arr)
        total = (n*(n+1))//2
        for i in arr:
            if i in s:
                repeat = i
            s.add(i)
            sum += i
        return [repeat,total-(sum-repeat)]
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends