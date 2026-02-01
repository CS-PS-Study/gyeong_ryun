import sys
# 데이터 개수, 질의 개수 저장
num, count = map(int, sys.stdin.readline().split())
# 데이터 리스트 저장
numbers = list(map(int, sys.stdin.readline().split()))

# 합리스트 생성
sum_list = [0] # 0번째 인덱스를 0으로 미리 채워줌
temp = 0

# 합리스트 채우기
for i in numbers:
    temp += i
    sum_list.append(temp) # 1번째 인덱스에 1번째 수의 합, 2번째 인덱스에는 1~2번쨰 수의 합... 
    
# 질의 처리
for _ in range(count):
    start , end = map(int, sys.stdin.readline().split())
    print(sum_list[end] - sum_list[start-1]) # start~end 까지의 수의 합