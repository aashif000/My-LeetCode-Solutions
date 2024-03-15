class Solution:
    def letterCombinations(self, s: str) -> List[str]:
        res = []
        d = {
            "2" :"abc",
            "3" :"def",
            "4" :"ghi",
            "5" :"jkl",
            "6" :"mno",
            "7" :"pqrs",
            "8" :"tuv",
            "9" :"wxyz"
        }
        
        def dfs(i,cur):
            if len(cur)==len(s):
                res.append(cur)
                return
            for j in d[s[i]]:
                dfs(i+1, cur+j)
        if s:
            dfs(0,'')
        return res