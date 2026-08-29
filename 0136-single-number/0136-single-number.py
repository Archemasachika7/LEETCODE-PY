class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d= {}
        n=len(nums)
        duplicate = True
        for i in range(n):
            if nums[i] not in d.keys() :
                d[nums[i]] = 1
            else :
                d[nums[i]] =d[nums[i]] + 1
        for key in d.keys():
            if d[key] == 1 :
                return key            

                   
            
        