class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        List1 = []
        for i in range(N):
            for j in range (i,N):
                if (i != j):
                    if (nums[i] + nums[j] == target):
                        List1.append(i)
                        List1.append(j)
        return List1