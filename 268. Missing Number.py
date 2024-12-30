class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        if (len(nums) == 0):
            return 0
        sorted_nums = sorted(nums)
        current_num=sorted_nums[0]
        for num in sorted_nums[1:]:
            if num != current_num+1:
                return current_num+1
            current_num = num
        return sorted_nums[len(nums)-1]+1
                
solution = Solution()
result = solution.missingNumber([1, 3, 4, 5, 6, 7])
print(result)