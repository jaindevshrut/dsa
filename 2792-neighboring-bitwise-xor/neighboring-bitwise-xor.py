class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        if derived[0] == 1 and len(derived) == 1:
            return False
        if derived[0] == 1:
            ans1 = [0,1]
            ans2 = [1,0]
            for i in range(1,len(derived)-1):
                if derived[i] == 0:
                    if ans1[-1] == 0:
                        ans1.append(0)
                    else:
                        ans1.append(1)
                    if ans2[-1] == 0:
                        ans2.append(0)
                    else:
                        ans2.append(1)
                if derived[i] == 1:
                    if ans1[-1] == 0:
                        ans1.append(1)
                    else:
                        ans1.append(0)
                    if ans2[-1] == 1:
                        ans2.append(0)
                    else:
                        ans2.append(1)
            if derived[-1] == ans1[-1] ^ ans1[0] or derived[-1] == ans2[-1] ^ ans2[0]:
                return True
        else:
            ans1 = [1,1]
            ans2 = [0,0]
            for i in range(1,len(derived)-1):
                if derived[i] == 0:
                    if ans1[-1] == 0:
                        ans1.append(0)
                    else:
                        ans1.append(1)
                    if ans2[-1] == 0:
                        ans2.append(0)
                    else:
                        ans2.append(1)
                if derived[i] == 1:
                    if ans1[-1] == 0:
                        ans1.append(1)
                    else:
                        ans1.append(0)
                    if ans2[-1] == 1:
                        ans2.append(0)
                    else:
                        ans2.append(1)
            if derived[-1] == ans1[-1] ^ ans1[0] or derived[-1] == ans2[-1] ^ ans2[0]:
                return True
        return False
