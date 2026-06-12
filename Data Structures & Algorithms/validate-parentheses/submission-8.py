class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        if len(s)==1:
            return False
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif ch in ")]}":
                if stack:
                    if (ch == ")" and stack.pop()=="(") or (ch == "}" and stack.pop()=="{") or (ch == "]" and stack.pop()=="["):
                        continue
                    else:
                        return False
                else:
                    return False
        return True if not stack else False
            
        