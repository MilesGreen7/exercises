class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = m - 1
        index2 = -1
        indexInsert = -1

        while index1 >= 0 and abs(index2) <= n:
            if nums2[index2] > nums1[index1]:
                nums1[indexInsert] = nums2[index2]
                index2 = index2 - 1
            else:
                nums1[indexInsert] = nums1[index1]
                index1 = index1 - 1
            indexInsert = indexInsert - 1
        
        while abs(index2) <= n:
            nums1[indexInsert] = nums2[index2]
            indexInsert = indexInsert - 1
            index2 = index2 - 1
