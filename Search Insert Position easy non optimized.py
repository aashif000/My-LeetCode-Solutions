class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #for i,v in enumerate(nums):
        #    if v==target:
        #        return i
        #for i in range(len(nums)-1,-1,-1):
        #    #print(nums[i])
        #    if target>nums[i]:
        #        return i+
        #if target not in nums:
        #    return 0
        if target in nums:
            return nums.index(target)
        else:
            i=0
            for j in nums:
                if j<target:
                    i+=1
                else:
                    break
            return i
