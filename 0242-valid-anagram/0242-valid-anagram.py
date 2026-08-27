class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lists = list(s)
        listt =list(t)
        n =len(s)
        p = len(t)
        ds = {}
        dt = {}
        
        for i in range(n):
            if (lists[i] not in ds.keys() ):
                ds[lists[i]] = 1
            else :
                ds[lists[i]] =    ds[lists[i]] + 1
        for j in range(p):
            if (listt[j] not in dt.keys() ):
                dt[listt[j]] = 1
            else :
                dt[listt[j]] =    dt[listt[j]] + 1        

        
        print (ds.items())
        print (dt.items())
               

        if (ds == dt and (n == p)) :
            return True
        return False    
            
        