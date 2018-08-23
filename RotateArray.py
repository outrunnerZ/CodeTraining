class Solution:         
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        reversePart(nums,0,len(nums)-1)
        reversePart(nums,k,len(nums)-1)
        reversePart(nums,0,k-1)
        
        
def reversePart(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1
