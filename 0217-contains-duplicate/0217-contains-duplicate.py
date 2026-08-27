class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n =len(nums)
        seen = list(set(nums))
        p = len(seen)
        if  (n == p ):
            return False
        else :
            return True    
        