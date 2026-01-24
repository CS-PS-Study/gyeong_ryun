import sys 
input = sys.stdin.readline # input() 대신 sys.stdin.readline() 사용
# n*n 표와 m번의 질의
n, m = map(int, input().split()) 

A = [] 
# n*n 표 입력받기
for _ in range(n): 
    A.append(list(map(int, input().split()))) 
    
# 구간 합 배열 D 구하기
D = [[0] * (n+1) for _ in range(n+1)] # (n+1)*(n+1) 크기의 0으로 초기화된 배열
for i in range(1, n+1):
    for j in range(1, n+1): 
        # 구간 합 계산
        D[i][j] = D[i][j-1] + D[i-1][j] + D[i-1][j-1] + A[i][j] 

# m번의 질의 처리        
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # x1,y1에서 x2,y2까지의 합 계산
    print(D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1])