class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        List2= [i for i in nums]
        for i in nums:
            List2.append(i)
        return List2
            
        