class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            # A
            i = (l + r) // 2
            # subtracts from both of the two arrays to account for of the arrays being off by 1 
            # B
            j = half - i - 2

            # left partiion in the smaller array
            if i >= 0:
                aLeft = A[i]
            else:
                aLeft = float("-infinity")

            if (i + 1) < len(A):
                aRight = A[i + 1]
            else:
                aRight = float("infinity")
            # if i or j is out of bounds
            if j >= 0:
                bLeft = B[j]
            else:
                bLeft = float("-infinity")

            if (j + 1) < len(B):
                bRight = B[j + 1] 
            else:
                bRight = float("infinity")
            
            # the partition is now correct
            if aRight < bRight and bLeft <= aRight:
                # odd
                if total % 2:
                    return min(aRight, bRight)
                # even
                return max(aLeft, bLeft) + min(aRight, bRight) // 2
            elif aLeft > bRight:
                # we have too many elements from A
                r = i - 1
            else:
                l = i - 1