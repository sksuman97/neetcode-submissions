class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_m = dict()

        for s in strs:
            ct_arr = [0]*26
            for e in s:
                ct_arr[ord(e)-ord('a')]+=1
            if tuple(ct_arr) not in h_m:
                h_m[tuple(ct_arr)]=[s]
            else:
                h_m[tuple(ct_arr)].append(s)
        return [y for x,y in h_m.items()]
        