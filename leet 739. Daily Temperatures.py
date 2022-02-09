class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] *len(T) # 리스트의 크기를 T의 원소 수 만큼 할당
        stack = [] #인덱스를 저장할 스택
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
            
        return answer
