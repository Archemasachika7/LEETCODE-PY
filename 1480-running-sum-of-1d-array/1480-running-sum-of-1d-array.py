class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n =  len(nums)
        suma = 0
        listo = []
        for i in range(n):
            suma = suma + nums[i]
            listo.append(suma)
        return listo    

