class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list1 =[]
        n = len(s)
        start = 0
        end = 0
        
        unique = False
        seen =[]
        if n ==1 :
            return 1
        if n == 0:
            return 0
        for i in range (n):
            
            while s[i] in seen :
                duplicate = True 
                
                seen.remove(s[start])
                start = start + 1
                
           
            seen.append(s[i])
            end = i + 1
              
            

           
                
            subs = s[start : end]    
            list1.append(len(subs))
        return (max(list1))