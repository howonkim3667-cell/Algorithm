def solution(my_string):
    my_string=my_string.lower()
    return ''.join(sorted(my_string))

# 파이썬 문자열 정렬은 sorted
# 리스트는 sort 사용 가능
# lower()는 힙 메모리의 값을 바꾸지 않고 반환해주기 때문에 변수 초기화 필요