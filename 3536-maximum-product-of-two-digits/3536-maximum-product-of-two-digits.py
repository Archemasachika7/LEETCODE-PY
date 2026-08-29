class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        product=[]
        while n != 0 :
            l.append(n%10)
            n = n // 10
        print (l)   
        prod = 1
        for i in range (len(l))  :
            for j in range (i,len(l)):
                if i!=j :
                    prod = l[i] * l[j]
                    product.append(prod)
                else:
                    continue
        return max(product)        

               

        