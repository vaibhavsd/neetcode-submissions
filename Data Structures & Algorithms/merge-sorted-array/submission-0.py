class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ctr1= 0
        ctr2= 0
        maxlen1= m
        maxlen2= n
        nums3= []
        while ctr1<maxlen1 or ctr2<maxlen2:
            if ctr1>= maxlen1:
                nums3.append(nums2[ctr2])
                ctr2+=1
            elif ctr2>= maxlen2:
                nums3.append(nums1[ctr1])
                ctr1+=1
            else:
                if nums1[ctr1]>nums2[ctr2]:
                    nums3.append(nums2[ctr2])
                    ctr2+=1
                else:
                    nums3.append(nums1[ctr1])
                    ctr1+=1
        print(nums3)

        for i in range(m+n):
            nums1[i]= nums3[i]
        return None
            

        