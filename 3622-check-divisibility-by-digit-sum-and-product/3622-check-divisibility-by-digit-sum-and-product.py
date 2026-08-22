class Solution:
    def checkDivisibility(self, n: int) -> bool:
        string = str(n)
        digsum =0 
        digprod =1
        list1 = []
        length = len(string)
        for i in range (length):
            list1.append(string[i])
        for i in range(length):
            digsum = digsum + int(list1[i]) 
            digprod = digprod * int(list1[i])
        
        condition1 = (n % (digsum + digprod) == 0)
        return condition1
        