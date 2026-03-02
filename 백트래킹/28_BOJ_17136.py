import sys
input = sys.stdin.readline

paper = [list(map(int, input().split())) for _ in range(10)]
cnt = [0] * 6   # cnt[i] = i×i 색종이 사용 횟수 (각 최대 5장)
ans = float('inf')

def can_attach(r, c, size):
    # 범위 벗어나면 False
    if r + size > 10 or c + size > 10:
        return False
    # 영역 안에 0이 있으면 False
    for i in range(r, r + size):
        for j in range(c, c + size):
            if paper[i][j] == 0:
                return False
    return True

def attach(r, c, size, val):
    # val=0 → 덮기, val=1 → 되돌리기
    for i in range(r, r + size):
        for j in range(c, c + size):
            paper[i][j] = val

def backtracking(r, c, total):
    global ans

    # 가지치기: 이미 ans 이상이면 의미 없음
    if total >= ans:
        return

    # 열이 끝나면 다음 행으로
    if c == 10:
        backtracking(r + 1, 0, total)
        return

    # 모든 행 탐색 완료 → ans 갱신
    if r == 10:
        ans = min(ans, total)
        return

    # 현재 칸이 0이면 다음 칸으로
    if paper[r][c] == 0:
        backtracking(r, c + 1, total)
        return

    # 현재 칸이 1이면 5×5 ~ 1×1 시도
    for size in range(5, 0, -1):
        if cnt[size] < 5 and can_attach(r, c, size):
            attach(r, c, size, 0)   # 색종이 붙이기
            cnt[size] += 1
            backtracking(r, c + 1, total + 1)
            attach(r, c, size, 1)   # 색종이 떼기 (백트래킹)
            cnt[size] -= 1

backtracking(0, 0, 0)
print(-1 if ans == float('inf') else ans)