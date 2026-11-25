from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        latest_data=dict(sorted(counter.items(), key = lambda item:item[1],reverse=True))
        results=[]
        count=0
        for num in latest_data:
            if count<k:
                results.append(num)
            count+=1
        return results