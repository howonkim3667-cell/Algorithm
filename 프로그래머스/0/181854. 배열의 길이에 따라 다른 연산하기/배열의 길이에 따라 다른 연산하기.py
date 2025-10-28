def solution(arr, n):
    if len(arr)%2:
        return [arr[i]+n if not i%2  else arr[i] for i in range(len(arr))]
    else:
        return [arr[i]+n if i%2  else arr[i] for i in range(len(arr))]
