class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) % 2 == 0 and len(nums2)%2 != 0:
            xor = 0
            for i in nums1:
                xor ^= i
            return xor
        elif len(nums1) % 2 == 0 and len(nums2)%2 == 0:
            return 0
        elif len(nums1) % 2 != 0 and len(nums2)%2 == 0:
            xor = 0
            for i in nums2:
                xor ^= i
            return xor
        else:
            xor = 0
            for i in nums1:
                xor ^= i
            for i in nums2:
                xor ^= i
            return xor

        