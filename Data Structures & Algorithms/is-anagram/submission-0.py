class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = dict()
        dt = dict()
        for cs in s:
            if cs in ds:
                ds[cs] = ds[cs] + 1
            else:
                ds[cs] = 1
        for ct in t:
            if ct in dt:
                dt[ct] = dt[ct] + 1
            else:
                dt[ct] = 1
        print(ds, dt)
        if dt == ds:
            return True
        return False