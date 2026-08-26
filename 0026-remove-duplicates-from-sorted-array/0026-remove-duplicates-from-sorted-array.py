class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        seen =[]
        n =len(nums)
        for i in range(n):
            if (nums[i] not in seen ):
                seen.append(nums[i])
        print(seen)
        nums.clear()
        nums.extend(seen)
        