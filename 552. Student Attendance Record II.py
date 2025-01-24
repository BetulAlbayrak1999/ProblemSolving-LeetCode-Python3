class Solution:
    MOD = 10**9 + 7

    def checkRecord(self, n: int) -> int:
        self.dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        return self.helper(n, 0, 0)

    def helper(self, n: int, counterA: int, counterL: int) -> int:
        if n == 0:
            return 1

        # Check if the result is already computed
        if self.dp[n][counterA][counterL] != 0:
            return self.dp[n][counterA][counterL]

        # initial result
        result = 0

        # Case 1: Add 'P' (Present) to the sequence
        result = (result + self.helper(n - 1, counterA, 0)) % self.MOD

        # Case 2: Add 'A' (Absent) if less than 1 'A' so far
        if counterA < 1:
            result = (result + self.helper(n - 1, counterA + 1, 0)) % self.MOD

        # Case 3: Add 'L' (Late) if less than 2 consecutive 'L's so far
        if counterL < 2:
            result = (result + self.helper(n - 1, counterA, counterL + 1)) % self.MOD

        # Store the result in the DP array
        self.dp[n][counterA][counterL] = result
        return result


solution = Solution()
result = solution.checkRecord(2)
print(result)
