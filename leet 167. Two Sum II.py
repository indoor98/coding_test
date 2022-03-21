# solution by using two pointer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while not left == right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            
            elif numbers[left] + numbers[right] < target:
                lett += 1
            
            else:
                return left+1, right+1 # in this problem, list starts from 1 not zero(0) so, we have to return +1
        
        return -1
      
# solution by using binary search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] > expected :
                    right = mid - 1
                    
                elif numbers[mid] < expected :
                    left = mid + 1
                
                else :
                    return k + 1, mid + 1
            
        return -1  
      
      
# solution3 - by using bisect module + slicing
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k+1:], expected)
            if i < len(numbers[k+1:]) and numbers[i+k+1] == expected:
                return k+1, i + k + 2
            
            
# solutin4 - optimization of solution3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k+1:]
            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and numbers[i+k+1] == expected:
                return k+1, i + k + 2
'''                  
bisect 모듈에 대한 파이썬 공식 문서 내용
bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
정렬된 순서를 유지하도록 a에 x를 삽입할 위치를 찾습니다. 매개 변수 lo 와 hi는 고려해야 할 리스트의 부분집합을 지정하는 데 사용될 수 있습니다; 
기본적으로 전체 리스트가 사용됩니다. x가 a에 이미 있으면, 삽입 위치는 기존 항목 앞(왼쪽)이 됩니다. 
반환 값은 a가 이미 정렬되었다고 가정할 때 list.insert()의 첫 번째 매개 변수로 사용하기에 적합합니다.
The returned insertion point i partitions the array a into two halves so that all(val < x for val in a[lo : i]) 
for the left side and all(val >= x for val in a[i : hi]) for the right side.
key specifies a key function of one argument that is used to extract a comparison 
key from each input element. The default value is None (compare the elements directly).
'''

# solution5 - optimization of solution4 (not using slicing)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, lo = k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k+1, i+1

'''
슬라이싱은 매우 효율적이고 빠르지만, 매번 새로운 객체를 생성해서 할당하게 되므로 배열의 크기가 커지면 그만큼 복사하는 과정이 길어져 시간이 오래 걸리게 된다.
따라서 특정 인덱스를 참조할 수 있는 경우에는 굳이 슬라이싱을 쓰지 않는게 좋을 수도 있다.
'''

