class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        3"""
        temp =[]
        n =len(nums) 
        reminder =0
        if (n > 1):
            if(k>0):
                if (k <= n ):
                    temp = nums[-k:] + nums[:n-k]
                    nums.clear()
                    nums.extend(temp)
                else :
                    reminder  = k%n
                    if (reminder != 0):
                        temp = nums[-reminder:] + nums[:n-reminder]   
                        nums.clear()
                        nums.extend(temp)
        
        


                
                


            

        