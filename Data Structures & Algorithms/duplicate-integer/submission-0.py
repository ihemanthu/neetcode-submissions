class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if not nums or len(nums) == 1:
            return False
        
        seen = {}

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 1

            else:
                return True
        return False
