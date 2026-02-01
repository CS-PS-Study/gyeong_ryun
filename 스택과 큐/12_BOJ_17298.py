import sys

n=int(sys.stdin.readline())
arr = []

# 입력 받기
for i in range(n):
    arr.append(int(sys.stdin.readline()))

result = [0] * n # 각 위치에서의 정답 저장용 배열 
stack = [] # (인덱스, 값) 쌍을 저장용 스택 

# 배열을 오른쪽에서 왼쪽으로 순회
for i in range(n,-1, -1, -1):
    # 스택에서 현재 값(arr[i])보다 작거나 같은 값은 제거!
    while stack and stack[-1] <= arr[i]:
        stack.pop()

    # 스택이 비어있지 않으면 top이 오큰수!
    if stack:
        result[i] = stack[-1]
    else:
        result[i] = -1

    # 다음 왼쪽 원소들을 위해 현재 값을 스택에 push
    stack.append(arr[i])

print(' '.join(map(str, result))) # 결과 출력 (공백으로 구분)