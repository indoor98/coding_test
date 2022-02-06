class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
        
#####
.sort(key)메서드는 정렬 기능을 한다.
key값을 기준으로 오름차순으로 정렬하며 두 개 이상의 key값을 줄 수 있다.
위 문제의 letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))을 해석해 보자
우선 letters에는 ["let1 art can", "let2 own kit dig","let3 art zero"]이 들어있다.
따라서 lambda x: (x.split()[1:], x.split()[0])에서 x는 letters에 들어있는 각각의 문자열이 되며, 뒤 스플릿 메서드를 통해 먼저 각각의 문자열의 두 번째 단어를 기준으로(순서대로 art, own, art)
오름차순 정렬을 한다 만일 두 번째 이후 단어들이 동일하다면 첫번째 단어를 기준으로 정렬하게 된다.
