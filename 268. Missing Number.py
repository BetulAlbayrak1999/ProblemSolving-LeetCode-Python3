class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sumOfNums= (len(nums) * (len(nums)+1))/2
        current_sum =0
        for num in nums:
            current_sum += num

        return int(sumOfNums- current_sum)
                
solution = Solution()
result = solution.missingNumber([0, 1, 3, 4, 5])
print(result)