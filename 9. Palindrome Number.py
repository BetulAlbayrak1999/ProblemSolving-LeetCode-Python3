class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = [digit for digit in str(x)]
        t1 = digits[::-1]
        t2=digits
        if(digits == digits[::-1]):
            return True
        return False
    
solution = Solution()
result = solution.isPalindrome(-121)
print(result)