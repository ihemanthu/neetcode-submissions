class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_length = len(nums)
        
        if not nums or nums_length == 1:
            return False
        
        seen = {}

        for i in range(nums_length):

            if nums[i] not in seen:
                seen[nums[i]] = 1
                
            else:
                return True

        return False
