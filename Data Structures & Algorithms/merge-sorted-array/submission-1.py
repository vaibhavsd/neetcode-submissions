class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        start1= m-1
        start2= n-1
        start= m+n-1
        for i in range(m+n-1, -1, -1):
            if start2<0:
                nums1[start]= nums1[start1] 
                start1-=1
                start-=1
            
            elif start1<0:
                nums1[start]= nums2[start2]
                start2-=1
                start-=1

            elif nums1[start1]>=nums2[start2]:
                nums1[start]= nums1[start1] 
                
                print(f'Assigning {nums1[start1]} to {start}')
                print(f'Start-{start}, start2- {start2}, start1- {start1}')
                start1-=1
                start-=1
            elif nums1[start1]<nums2[start2]:
                nums1[start]= nums2[start2]
                
                print(f'Assign {nums2[start2]} to {start}')
                print(f'Start-{start}, start1- {start1}')
                start2-=1
                start-=1
        
            
            