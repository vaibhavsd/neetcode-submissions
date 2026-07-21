class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ptr= 0
        slow=nums[0]
        fast=nums[nums[0]]
        while slow!=fast:
            slow= nums[slow]
            fast= nums[nums[fast]]
        
        print(f'Cycle is now found at slow- {slow}, fast- {fast}')

        slow= 0
        while slow!=fast:
            slow= nums[slow]
            fast= nums[fast]
        return slow

