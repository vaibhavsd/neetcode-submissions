class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        mdict= Counter(nums)
        sorted_data_desc = dict(sorted(mdict.items(), key=lambda item: item[1], reverse=True))
        
        mout= list(sorted_data_desc.keys())[:k]
        return mout