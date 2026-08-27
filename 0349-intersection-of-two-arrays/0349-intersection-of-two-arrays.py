class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:



        set1 = set(nums1)
        set2 = set(nums2)
        list1 = list(set1)
        list2 =list(set2)
        n = len(list1)
        m = len(list2)
        seen =[]
        if n >= m :
            for i in range (n):
                if list1[i] in list2 :
                    seen.append(list1[i])

        if m > n :
            for j  in range (m):
                if list2[j] in list1:
                    seen.append(list2[j])
        print (seen)
        return (seen)  