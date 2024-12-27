import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       return math.comb(m+n-2, m-1) 

solution = Solution()
result = solution.uniquePaths(3, 7)
print(result)