class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len (prices)
        profit = True
        List = []
        minimum  = prices[0]
        maximum = prices[0]
        maxindex =0
        minindex = 0
        
        for i in range (n) :
            if prices[i] < minimum :
                minimum = prices[i]
                minindex = i
            if prices[i] > maximum :
                maximum  =  prices[i]
                maxindex = i
            
            if (minindex >= maxindex ):
                maximum = minimum
            if (minindex < maxindex):
                List.append(maximum - minimum)
        if len(List) == 0 :
            return 0
        else:
            return max(List)              

        
             
        


