class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        words_list=[]
        for word in strs:
            words_list.append(list(word))
        result = words_list
        return ""
solution = Solution()
result = solution.longestCommonPrefix(["word", "woooff", "womna"])
print(result)