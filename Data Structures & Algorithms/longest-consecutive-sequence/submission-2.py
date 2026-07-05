class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import defaultdict
        hashmap= defaultdict(int)
        maxcount= 0

        for i in range(len(nums)):
            hashmap[nums[i]]= False
        
        for i in range(len(nums)):
            if hashmap[nums[i]]==True:
                continue
            else:
                hashmap[nums[i]]=True

                count= 1
                val= nums[i]
                while True:
                    if val+1 in hashmap.keys():
                        hashmap[val+1]=True
                        val= val+1
                        count+=1
                        print(f'Increasing count at {val}')
                    else:
                        break
                val= nums[i]
                while True:
                    if val-1 in hashmap.keys():
                        hashmap[val-1]=True
                        val= val-1
                        count+=1
                    else:
                        break
                if count>maxcount:
                    maxcount= count
        return maxcount        
                        
                    





