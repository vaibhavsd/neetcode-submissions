class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        minlen= 999999999
        left= 0
        right= 0
        
        currlen= 1
        currsum= nums[0]
        while right<= len(nums)-1:

            if currsum>=target:
                if currlen<minlen:
                    minlen= currlen
                    #print(f'Left- {left}, Right- {right}')
                
                while currsum>=target:
                    #print(f'currsum- {currsum}')
                    currsum-=nums[left]
                    left+=1
                    currlen-=1
                    #print(f'Left increased to - {left}')

                    if currlen<minlen and currsum>=target:
                        minlen= currlen

            else:
                if right+1<= len(nums)-1:
                    
                    right+=1
                    currlen+=1
                    currsum+=nums[right]
                    #print(f'Right increased to - {right}')
                else:
                    break
        
        if currlen<minlen and currsum>=target:
            minlen= currlen
        if minlen== 999999999:
            minlen= 0
        return minlen