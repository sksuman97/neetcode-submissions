class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_={}
        for s in strs:
            sort_s = ''.join(sorted(s))
            if sort_s not in dict_:
                dict_[sort_s]=[s]
            else:
                dict_[sort_s].append(s)
        return [y for x,y in dict_.items()]
        