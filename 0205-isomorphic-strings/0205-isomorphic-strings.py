class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        p = len(t)
        d={}
        m={}
        si=False
        ti=False
        if n == p :
            for i in range (n) :
                
                if s[i] not in d.keys() :
                    d[s[i]] = t[i]
                    si=True
                elif s[i] in d.keys() :
                    
                    if d[s[i]] == t[i] :
                        si=True
                        
                    else:
                        ti = False
                        break 
                if t[i] not in m.keys() :
                    m[t[i]] = s[i]
                    ti=True
                elif t[i] in m.keys() :
                    if m[t[i]] == s[i] :
                        ti=True
                    else:
                        ti = False
                        break        
                

            if ( si == True  )and (ti == True):
                return True 
            return False
        return False                        



            



        