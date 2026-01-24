n = int(input())

answer = 1  # n 자기 자신도 하나의 경우의 수
left = 1    # 시작 포인터
right = 1   # 끝 포인터
total = 1   # 현재 구간의 합 (left부터 right까지)

while right != n:
    if total == n:  # 합이 n과 같으면
        answer += 1       # 경우의 수 증가
        right += 1        # 오른쪽 포인터 이동
        total += right    # 새로운 값 추가
    elif total > n:  # 합이 n보다 크면
        total -= left     # 왼쪽 값 제거
        left += 1         # 왼쪽 포인터 이동
    else:  # 합이 n보다 작으면
        right += 1        # 오른쪽 포인터 이동
        total += right    # 새로운 값 추가

print(answer)