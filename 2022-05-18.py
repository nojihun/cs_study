"""
이진 트리 안쓴 버전
"""
def search( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        count = 1
        
        for i in nums:
            if i == target:
                break
            count+=1
            
        if count > len(nums):
            return -1
        
        return count -1

"""
이진트리 버전
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) //2 
            
            if nums[mid]<target:
                left = mid+1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid
        return -1