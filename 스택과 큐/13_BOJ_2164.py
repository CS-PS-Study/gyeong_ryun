from collections import deque

n = int(input()) # 카드 개수
my_queue = deque()

# 1부터 n까지의 카드를 덱에 순서대로 추가
for i in range(1, n+1):
    my_queue.append(i)

# 카드가 1장 남을 때까지 반복
while len(my_queue) > 1:
    my_queue.popleft() # 맨 위 카드 제거 
    my_queue.append(my_queue.popleft()) # 맨 위 카드를 젤 아래 밑에 깔아

print(my_queue[0]) # 최종 남은 카드 출력