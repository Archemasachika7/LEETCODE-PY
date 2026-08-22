class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sume =[]
        cutie =  False

        for i in range (n):
            left =  sum(nums[:i])
            right = sum(nums[i+1:])
            if (left == right):
               cutie = True
               index = i
               break
        if (cutie == True):
            return index
        else :
            return -1    

            



           