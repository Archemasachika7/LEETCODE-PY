class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        inter=[]
        for st in strs:
            l=sorted(st)
            s="".join(l)
            if s not in d.keys():
                d[s] = [st]
            else :
                d[s].append(st)
         
        for key in   d.keys():
            inter.append(d[key])
        return inter    
                     


        '''n=len(strs)
        inter=[]
        d={}
        g=[]
        seen =[]
                
        for i in range (n):
            for j in range (i,n):
                if isvalid(strs[i],strs[j]):
                    if strs[i] not in seen :
                        g.append(strs[i])
                    if strs[j] not in seen :    
                        g.append(strs[j])
            print (g)     '''


                                
                
               
        