'''
Created on Jan 5, 2018

@author: Jake
'''
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if(m == 0):
            for x in range(n):
                nums1[x] = nums2[x]
        else:
            spot = len(nums1) - n
            for x in range(n):
                nums1[spot] = nums2[x]
                spot += 1
            nums1.sort()