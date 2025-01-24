from functools import lru_cache


class Solution:

    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        # Use @lru_cache to memorize results
        @lru_cache(None)
        def helper(days_left: int, absents: int, lates: int) -> int:
            if days_left == 0:
                return 1

            result = 0

            # Case 1: Add 'A' (reset lates to 0)
            result += helper(days_left - 1, absents, 0)

            # Case 2 : Add 'A' (increment absents if less than 1)
            if absents < 1:
                result += helper(days_left - 1, absents + 1, 0)

            # Case 3: Add 'L' (increment lates if less than 2)
            if lates < 2:
                result += helper(days_left - 1, absents, lates + 1)

            return result % MOD

        return helper(n, 0, 0)


solution = Solution()
result = solution.checkRecord(1)
print(result)
