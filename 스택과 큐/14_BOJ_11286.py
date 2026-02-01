import heapq
import sys

input = sys.stdin.readline

n = int(input()) # 연산 개수
heap = [] # 우선순위 큐 역할을 할 최소 힙
result = []

for _ in range(n):
    x = int(input()) # 입력값

    # x가 0이면 배열에서 절댓값이 가장 작은 값을 출력하고 제거
    if x == 0: 
        # 힙이 비어있으면 0 출력
        if not heap:
            result.append(0)

        # 아니라면 힙에서 최솟값을 꺼내서 제거 및 출력
        else:
            result.append(str(heapq.heappop(heap)[1])) 
    
    # x가 0이 아니면면 배열에 x를 추가
    else:
        # (절댓값, 원본값) 튜플 형태로 저장
        # 절댓값이 같으면 원본값으로 비교하기 위해 튜플 사용
        heapq.heappush(heap, (abs(x), x))

print('\n'.join(result))