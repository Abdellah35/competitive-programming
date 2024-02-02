class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        fr = min(strs, key=len)
        commmon = ""
        for i in range(len(fr)):
            for st in strs:
                if st[i] == fr[i]:
                    continue
                else:
                    return commmon
            commmon += st[i]
        return commmon
        
