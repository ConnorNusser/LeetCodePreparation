class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        
        for i in range(0, len(nums) - 1):
            for y in range(1, len(nums)):
                if nums[i] + nums[y] == target and i != y:
                    return [i, y]
        