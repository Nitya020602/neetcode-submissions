class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictn={}
        for string in strs:
            key=str(sorted(string))
            if key in dictn:
                dictn[key].append(string)
            else:
                dictn[key]=[string]
        result=[]
        for key in dictn:
            result.append(dictn[key])
        return result