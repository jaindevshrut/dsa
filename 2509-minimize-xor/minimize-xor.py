class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = 0
        while num2:
            count += num2 & 1
            num2 >>= 1
        ans = ''
        t = bin(num1)[2:]
        for i in t:
            if i == '1' and count:
                ans += '1'
                count -= 1
            else:
                ans += '0'
        if count > 0:
            for i in reversed(range(len(ans))):
                if ans[i] == '0' and count:
                    ans = ans[:i] + '1' + ans[i+1:]
                    count -= 1
            if count > 0:
                ans += '1'*count
        return int(ans,2)
        