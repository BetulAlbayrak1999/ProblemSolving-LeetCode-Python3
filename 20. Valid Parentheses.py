class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        matching_brackets = {")":"(",  "}":"{" ,  "]":"["  }
        stack= []
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")]}":
                if not stack or stack[-1] != matching_brackets[char]:
                    return False
                stack.pop()
        return not stack
                
solution = Solution()
result = solution.isValid("{()()}")
print(result)