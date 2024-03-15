class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = []
        if len(s)<=10:
            return []
        def cf(my_list):
            freq = {}
            for item in my_list:
                if (item in freq):
                    freq[item] += 1
                else:
                    freq[item] = 1
            return freq 
        
        
        for i in  range(len(s)-9):
            ts = ""
            for j in range(i,i+10):
                ts+=s[j]
            
            l.append(ts)
        d = cf(l) 
        print(d)
        res = []
        for i in d:
            if d[i]>=2:
                res.append(i)
        return res
