# 브루트포스를 이용한 풀이
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: set = set()
            
        for i in nums1:
            for j in nums2:
                if i == j:
                    result.add(i)
                    
        return result                
    
# 이진탐색을 이용한 풀이
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: set = set()
        nums2.sort()
        for n1 in nums1:
            i2 = bisect.bisect_left(nums2, n1)
            #예외처리
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)
        
        return result
      
# 투 포인터를 이용한 풀이
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: set = set()
        #sort()의 시간복잡도는 O(nlog(n))이다
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else :
                result.add(nums1[i])
                i += 1
                j += 1
            
        return result
 
