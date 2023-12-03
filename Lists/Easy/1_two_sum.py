"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first_num = nums[0]
        first_index = 0
        x = target - first_num
        rtype = []
        
        for num in nums:
            if x in nums:
                x_index = nums.index(x)
                if x_index != first_index:
                    rtype.append(first_index)
                    rtype.append(x_index)
                    break
                else:
                    first_index += 1
                    if first_index <= (len(nums) - 1):
                        first_num = nums[first_index]
                        x = target - first_num
                    else:
                        break
            else:
                first_index += 1
                if first_index <= (len(nums) - 1):
                    first_num = nums[first_index]
                    x = target - first_num
                else:
                    break
                    
        if len(rtype) > 0:
            rtype.sort()
            
        return rtype


class_obj = Solution()
nums = [2,7,11,15]
target = 26

print(class_obj.twoSum(nums, target))
