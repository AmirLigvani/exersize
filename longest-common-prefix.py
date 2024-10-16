class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for l in range(1, len(strs[0])+1):
            op = strs[0[0:l]]
            for s in str[1:]:
                if len(s) < L or s[o:l] != op:
                    return ans
                ans = op
        return ans