class Solution:
    def isValid(self, s: str) -> bool:
        p = []
        if len(s) % 2 == 1:
            return False
        for x in s:
            print(p)
            if x == "(":
                p.append("(")
            if x == "{":
                p.append("{")
            if x == "[":
                p.append("[")
            if x == ")":
                if(p == [] or p.pop() != '('):
                    return False
            if x == "}":
                if(p == [] or p.pop() != '{'):
                    return False
            if x == "]":
                if(p == [] or p.pop() != '['):
                    return False
        if p == []:
            return True
        else:
            return False