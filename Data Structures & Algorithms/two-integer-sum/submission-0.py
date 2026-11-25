class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictn={}
        for ind,num in enumerate(nums):
            if target-num in dictn:
                return [dictn[target-num],ind]
            dictn[num]=ind
        return [-1,-1]
        