class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxcount = 0
        n = len(nums)
        target = (n//2)
        seen = []
        d = {}
        for i in range (n):
            if (nums[i] in seen):
                d[nums[i]] = d[nums[i]] + 1
            else :
                seen.append(nums[i])
                d[nums[i]] = 1
        for key,value in d.items():
            if ( value > target ):
                return (key)



