from collections import deque
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid_len1 = (len(nums1) + len(nums2) - 1) // 2
        mid_len2 = (len(nums1) + len(nums2)) // 2
        nums1 = deque(nums1)
        nums2 = deque(nums2)
        a, b = 0, 0
        for i in range(mid_len2 + 1):
            if len(nums1) == 0:
                t = nums2.popleft()
            elif len(nums2) == 0:
                t = nums1.popleft()
            elif nums1[0] > nums2[0]:
                t = nums2.popleft()
            else:
                t = nums1.popleft()
            if i == mid_len1:
                a = t
            if i == mid_len2:
                b = t
        return (a + b) / 2


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1], []))
