class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        traversal_len= len(nums)- k + 1
        maxarr= []

        from collections import deque
        mdeck= deque()
        for i in range(k-1):
            mdeck.append(nums[i]) 

        for i in range(traversal_len):           
            mdeck.append(nums[i+k-1])
            maxarr.append(max(mdeck))
            mdeck.popleft()
            
        return maxarr 