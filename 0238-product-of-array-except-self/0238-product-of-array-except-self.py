class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        
        prod = 1
        post=1
        prev=[]
        pos=[]
        d={}
        ans=[]
        prev.append(prod)
        for i in range (1,n) :
            prod = prod * nums[i-1]
            prev.append(prod)
            

             
        re = nums[::-1]
        
        t=len(re)
        pos.append(post)
        for j in range (1,t):
            post = post * re[j-1]
            
            pos.append(post)
           


        

         
        
        npos=pos[::-1]
        
        for k in range(n):
            ans.append(prev[k]*npos[k])
        return ans 



       
              

        