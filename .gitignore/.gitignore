class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=0:
            return False
        buff_dist = {}
        for i in range(len(nums)):
            if nums[i] in buff_dist:
                return [buff_dist[nums[i]], i]
            else:
                buff_dist[target-nums[i]] = i
