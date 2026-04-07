class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        total = len(nums1) + len(nums2)
        half = total // 2 
        l = 0
        r = len(nums1) - 1
        while True:
            i = (l+r)//2
            j = half - i - 2

            l1 = nums1[i] if i >= 0 else float('-inf')
            r1 = nums1[i+1] if i+1 < len(nums1) else float('inf')
            l2 = nums2[j] if j >= 0 else float('-inf')
            r2 = nums2[j+1] if j+1 < len(nums2) else float('inf')

            if l1 <= r2 and l2 <= r1:
                if total % 2 :
                    return float(min(r1,r2))
                else:
                    return float((max(l1,l2) + min(r1,r2))/2)
            elif l1 > r2:
                r = i - 1
            else:
                l = i + 1



