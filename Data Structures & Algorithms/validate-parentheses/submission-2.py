class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open = {"]":"[", ")":"(", "}":"{"}
    

        for c in s:
            if c in close_open:
                if not stack or stack[-1] != close_open[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return (stack == [])
            