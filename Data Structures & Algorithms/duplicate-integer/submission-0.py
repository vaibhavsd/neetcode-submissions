class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset= set(nums)
        return not len(myset)== len(nums)
        