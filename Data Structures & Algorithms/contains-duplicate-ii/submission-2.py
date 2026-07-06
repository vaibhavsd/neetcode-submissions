class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mydict= dict()

        for i in range(len(nums)):
            if nums[i] in mydict.keys():
                print(f'{i}-{nums[i]}')
                if abs(i- mydict[nums[i]])<=k:
                    return True
                else:
                    mydict[nums[i]]= i
            else:
                mydict[nums[i]]= i
                print(f'False {i}-{nums[i]}')
        return False