class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        r = []
        for s in strs:
            x = sorted(s)
            x = "".join(x)
            #print(d,s,x)
            if x in d:
                n = d[x]
                n.append(s)
                d[x] = n
            else:
                d[x] = [s]
        print(d)
        for k in d:
            r.append(d[k])
        return r
