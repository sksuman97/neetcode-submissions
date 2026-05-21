class Solution:
    def isPalindrome(self, s: str) -> bool:
        orig_l = []
        for st in s:
            if st.isalnum():
                orig_l.append(st.lower())
        orig_st = ''.join(orig_l)
        ## Reverse string
        rev_l = []
        for st in s[::-1]:
            if st.isalnum():
                rev_l.append(st.lower())
        rev_st = ''.join(rev_l)
        if orig_st==rev_st:
            return True
        return False