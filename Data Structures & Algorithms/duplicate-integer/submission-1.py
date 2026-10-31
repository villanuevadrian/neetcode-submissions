class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            num = nums.pop()
            if num in nums:
                return True
        return False
