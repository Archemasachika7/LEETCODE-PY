class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        
        temp=[]
        for i in range (m):
            
            temp.append(nums1[i])
        temp.extend(nums2)
        nums1.clear()
        nums1.extend(temp)
        nums1.sort()
        

        