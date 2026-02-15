from collections import deque

n, window = map(int, input().split())
dq = deque()
numbers = list(map(int, input().split()))

for i in range(n):
    # 현재 값보다 큰 값들을 deque 뒤에서 제거
    while dq and dq[-1][0] > numbers[i]:
        dq.pop()
    
    # 현재 값과 인덱스 추가
    dq.append((numbers[i], i))
    
    # 윈도우 범위를 벗어난 값 제거
    if dq[0][1] <= i - window:
        dq.popleft()
    
    # 현재 윈도우의 최솟값 출력
    print(dq[0][0], end=' ')