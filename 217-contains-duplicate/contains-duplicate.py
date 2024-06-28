class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tempSet = set(nums)
        if len(tempSet) != len(nums):
            return True

        