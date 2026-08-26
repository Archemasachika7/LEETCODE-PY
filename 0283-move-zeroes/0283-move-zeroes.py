class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp=[]
        count = nums.count(0)
        for i in range (n):
            if (nums[i] != 0 ):
                temp.append(nums[i])
                
        for i in range (count):
            temp.append(0)
        nums.clear()
        nums.extend(temp)

         
            
              
            
                
        