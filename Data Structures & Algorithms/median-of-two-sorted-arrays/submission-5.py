class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1 = len(nums1)
        n2 = len(nums2)
        total = n1 + n2
        half = total // 2
        l = 0
        r = n1 - 1
        while True:
            i = (l+r) // 2
            j = half - i - 2

            al = nums1[i] if i >= 0 else float('-inf')
            ar = nums1[i+1] if i < n1-1 else float('inf')
            bl = nums2[j] if j >= 0 else float('-inf')
            br = nums2[j+1] if j < n2-1 else float('inf')

            if al <= br and bl <= ar:
                if (total % 2):
                    return min(ar,br)
                else:
                    return (max(al,bl) + min(ar,br))/2
            elif al > br:
                r = i - 1
            else:
                l = i + 1



