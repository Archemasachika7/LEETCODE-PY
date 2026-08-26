class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        seen =[]
        n =len(nums)
        for i in range(n):
            if (nums[i] not in seen ):
                seen.append(nums[i])
        print(seen)
        nums.clear()
        nums.extend(seen)
        