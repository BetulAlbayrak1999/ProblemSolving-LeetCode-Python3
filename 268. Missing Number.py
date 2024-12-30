class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)

        if (nums[0]!= 0):
            return 0

        current_num=nums[0]
        for num in nums[1:]:
            if num != current_num+1:
                return current_num+1
            current_num = num
        return nums[len(nums)-1]+1
                
solution = Solution()
result = solution.missingNumber([1, 3, 4, 5, 6, 7])
print(result)