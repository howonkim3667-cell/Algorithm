def solution(age):
    age = str(age)
    answer = ''
    for i in range(len(age)):
        b = int(age[i]) + 97
        answer+=chr(b)
    
    
    return answer

## 아스키 코드 알파벳 소문자는 97 == 'a' 부터 시작
## chr() 함수 사용해서 숫자를 아스키코드로 변환