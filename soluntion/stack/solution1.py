


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            elif not stack:
                return False
            else:
                left = stack.pop()
                if ch == ')' and left == '(':
                    continue
                if ch == ']' and left == '[':
                    continue
                if ch == '}' and left == '{':
                    continue
                return False
        if stack:
            return False
        return True

                