class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            component = target - nums[i]
            if component in nums[i+1:]:
                if (component == nums[i]):
                    j = nums.index(nums[i],i+1)
                    return [i,j]
                j = nums.index(component)
                return[i,j]
           