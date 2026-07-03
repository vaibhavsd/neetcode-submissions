class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numslen= len(nums)
        for i in range(numslen):
            nums.append(nums[i])
        return nums