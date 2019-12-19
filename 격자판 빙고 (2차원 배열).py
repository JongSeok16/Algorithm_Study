# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합 니다.
# n = 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

# 위의 문제는 2중 배열을 사용하여 각 인덱스의 번호의 규칙을 찾아서 풀면 해결됨


n = int(input())
ls = []  # 격자판
for i in range(n):
    lss = list(map(int, input().split()))
    ls.append(lss)

result = 0  # 최종 반환 값

# 가로 최대 값

for i in range(len(ls)):
    total = 0  # 각 행에 있는 값들을 더한 변수
    for e in range(len(ls[i])):
        total = total + ls[i][e]
        # 10 13 10 12 15 => ls[0][0] = 10
        # 12 39 30 23 11 => ls[0][1] = 13
        # 11 25 50 53 15 => ls[0][2] = 10
        # 19 27 29 37 27 => ls[0][3] = 12
        # 19 13 30 13 19 => ls[0][4] = 15
    if result < total:  # 현재 행의 값이 더 클 경우 result에 현재 행의 값으로 초기화
        result = total

# 세로 최대 값

for i in range(len(ls)):
    total = 0  # 각 열에 있는 값들을 더한 변수
    for e in range(len(ls[i])):
        total = total + ls[e][i]
        # 10 13 10 12 15 => ls[0][0] = 10
        # 12 39 30 23 11 => ls[1][0] = 12
        # 11 25 50 53 15 => ls[2][0] = 11
        # 19 27 29 37 27 => ls[3][0] = 19
        # 19 13 30 13 19 => ls[4][0] = 19
    if result < total:  # 행에서 가장 큰값과 현재 열의 값을 비교해 현재 열이 더 클 경우
        result = total  # 현재 열에 해당하는 값으로 초기화

# 대각선 최대 값

for i in range(len(ls)):
    total = 0
    total2 = 0
    for e in range(len(ls[i])):
        total = total + ls[e][e]  # 대각선 1
        # 10 13 10 12 15 => ls[0][0] = 10
        # 12 39 30 23 11 => ls[1][1] = 39
        # 11 25 50 53 15 => ls[2][2] = 50
        # 19 27 29 37 27 => ls[3][3] = 37
        # 19 13 30 13 19 => ls[4][4] = 19

        total2 = total2 + ls[e][-1 - e]  # 대각선 2

        # 10 13 10 12 15 => ls[0][-1] = 15
        # 12 39 30 23 11 => ls[1][-2] = 23
        # 11 25 50 53 15 => ls[2][-3] = 50
        # 19 27 29 37 27 => ls[3][-4] = 27
        # 19 13 30 13 19 => ls[4][-5] = 19

    if result < total:
        result = total
    if result < total2:
        result = total2
    break

print(result)
