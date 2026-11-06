class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            component = target - nums[i]
            if component in nums[i+1:]:
                j = nums.index(component,i+1)
                return[i,j]
           