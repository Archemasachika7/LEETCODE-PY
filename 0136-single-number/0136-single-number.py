class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = []
        n=len(nums)
        duplicate = True
        for i in range(n):
            if nums.count(nums[i]) == 1 :
                return nums[i]
                   
            
        