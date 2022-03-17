# 재귀함수 풀이
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(left, right):
            if left <= right:
                mid = (left + right)//2
                
                if nums[mid] == target:
                    return mid
                
                elif nums[mid] < target:
                    return binary_search(mid+1, right)
                
                else:
                    return binary_search(left, mid-1)
                
            else :
                return -1
            
        return binary_search(0, len(nums)-1)

# 반복을 이용한 풀이
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2
            
            elif nums[mid] > target:
                right = mid - 1
                mid = (left + right) // 2
                
            else :
                return mid
        return -1
        
        
        
        
