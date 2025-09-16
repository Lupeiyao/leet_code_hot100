


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != '[':
                stack.append(stack)
            else:
                # 找到中括号中的字符串
                sub_str = []
                tmp = stack.pop()
                while tmp != '[':
                    sub_str.insert(0, tmp)
                    tmp = stack.pop()
                # 找到中括号前的数字
                num_str = []
                while stack and '0' <= stack[-1] <= '9':
                    num_str.insert(0, stack.pop())
                # 构造3[a]->aaa并放入stack
                stack.extend("".join(sub_str) * int("".join(num_str)))
        return "".join(stack)
    
print(Solution().decodeString("100[leetcode]"))
                