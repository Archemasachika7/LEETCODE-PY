class Solution:
    def isHappy(self, num: int) -> bool:
        happy = False
        seen=[]
        def digitsum(n):    
            digits =[]
            while (n != 0) :
                digits.append(n%10)
                n =  (n // 10)
                
             
            summ = 0
            for i in range(len(digits)):
                summ = summ + digits[i]**2
            return summ
        digi = digitsum(num)    
        while digi != 1 :
            
            
            
            
                 
            
            if digi in seen :
                return False 
            if digi not in seen :
                seen.append(digi) 
            digi = digitsum(digi) 
            print (seen)  
                    
                
        return True       





        