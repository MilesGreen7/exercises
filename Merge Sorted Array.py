class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1 = nums2
            return
        if n == 0:
            return

        index1 = 0
        index2 = 0
        indexInsert = m


        