class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        ans=[]
        for num in nums :
            if num not in d.keys():
                d[num] = 1
            else :
                d[num] =d[num] + 1
        for key in d.keys():
            l.append(d[key])
        l.sort()   
        l=l[::-1]
        
        frq = l[k-1]
        for key in d.keys():
            if d[key] >= frq :
                ans.append(key)
        
        return ans        
               


           
        