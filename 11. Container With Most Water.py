import math


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right, max_container = 0, len(height) - 1, 0
        while left < right:
            current_container = (right - left) * min(height[left], height[right])
            max_container = max(current_container, max_container)
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_container


solution = Solution()
result = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
