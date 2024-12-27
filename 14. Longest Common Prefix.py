class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        result = strs[0]
        
        for word in strs[1:]:
            while not word.startswith(result):
                result= result[:-1] # Remove the last character
        return result
    
solution = Solution()
result = solution.longestCommonPrefix(["flower", "flow", "fl"])
print(result)