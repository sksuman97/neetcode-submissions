class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs ==[]:
            return ''
        ## We will create two separate section for the final str
        count = [str(len(st)) for st in strs]
        return ','.join(count)+'#'+''.join(strs)

    def decode(self, s: str) -> List[str]:
        if s=='':
            return []
        ## Splitting the results into count/str
        # To spllit the string when we see the first #
        i = 0
        while s[i]!='#':
            i+=1
        count, str_ = s[:i], s[i+1:]
        print(count, str_)
        res = []
        c = 0
        counts = count.split(',')

        for l in counts:
            # print(l)
            res.append(str_[c:c+int(l)])
            c += int(l)
        return res