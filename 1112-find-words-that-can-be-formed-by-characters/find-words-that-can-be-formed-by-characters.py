class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = 0 
        def comp(a,b):
            c = 0
            for i in a:
                if b.count(i)<a.count(i):
                    return 0
                c+=1
            return c
        for i in words:
            c+=comp(i,chars)
        return c