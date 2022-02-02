#투 포인터를 이용한 풀이
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            
            else :
                volume += right_max - height[right]
                right -= 1
                
        return volume
      
# 스택을 이용한 풀이
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] #스택에는 height의 각 원소의 인덱스가 들어간다.
        volume = 0
        for i in range(len(height)):
            #변곡점일 경우, 즉 이전 높이보다 현재 높이가 더 높을 경우
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not len(stack):
                    break
                
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volume += distance * waters
            stack.append(i)
        return volume
