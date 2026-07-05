class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if nums is []:
            return 0
        maxsum= nums[0]
        currsum= 0

        for i in range(len(nums)):
            if currsum<0:
                currsum= 0
            currsum+=nums[i]

            if maxsum<currsum:
                maxsum=currsum
                print(f'maxsum updated on {nums[i]} to {maxsum}')
        return maxsum