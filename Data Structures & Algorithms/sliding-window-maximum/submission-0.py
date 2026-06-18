class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        traversal_len= len(nums)- k + 1
        maxarr= []
        for i in range(traversal_len):
            maxelem= -100000
            for j in range(k):
                elem= nums[i+j]
                maxelem= max(elem, maxelem)
            maxarr.append(maxelem)
        return maxarr