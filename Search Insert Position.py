class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            if target > nums[-1]:
                return len(nums)
            if target < nums[0]:
                return 0
            L = 0
            R = len(nums) - 1
            while L < R - 1:
                mid = (R + L) // 2
                print(L, R, mid)
                if nums[mid] > target:
                    R = mid
                else: 
                    L = mid
            return L + 1

            return start + 1
