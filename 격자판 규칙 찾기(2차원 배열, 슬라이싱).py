# 현수의 농장은 N*N 격자판으로 이루어져 있으며,
# 각 격자안에는 한 그루의 사과나무가 심어저 있다.
# N의 크기는 항상 홀수이다.
# 가을이 되어 사과를 수확해야 하는데
# 현수는 격자판안의 사 과를 수확할 때 다이아몬드 모양의 격자판만 수확하고
# 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.

# 10 13 10 12 15            10
# 12 39 30 23 11         39 30 23
# 11 25 50 53 15      11 25 50 53 15
# 19 27 29 37 27         27 29 37
# 19 13 30 13 19            30

# 수확한 사과의 총 개수를 출력합니다.


# 위의 문제는 가장먼저 격자판을 2차원 배열로 생성한 뒤
# 다이아몬드 모양의 특성을 보면 중심이 되는 부분부터 1칸씩 증가하다
# 중심이 되는 부분을 지나는 순간부터 1칸씩 감소하는 특징이 있음

# 그렇다면 중간 값을 먼저 구한 뒤 해당 값을 기준으로 증가 or 감소시키면서 값을 구하면 됨


n = int(input())
cen = n // 2  # 중심이 되는 값을 cen 변수에 할당
ls = []  # 격자판
result = []  # 다이아몬드에 해당하는 부분을 담을 배열
total = 0  # 최종적으로 더한 값

for i in range(n):
    lss = list(map(int, input().split()))
    ls.append(lss)

for i in range(len(ls)):
    # 해당 문제를 푸는 방법으로 중간값을 기준으로
    # 앞과 뒤를 나누어 해당 배열을 슬라이싱함
    # 슬라이싱 한 배열의 값을 하나씩 빼오면서
    # total 이라는 변수에 계속 더해 나갈 거임

    # 중간값 ex) 2 일시
    front = abs(i - cen)
    # [ front : back ] => front = 2
    # [ front : back ] => front = 1
    back = -(abs(cen - i))
    # [ front : back ] => back = -2
    # [ front : back ] => back = -1
    if i != cen:
        result = ls[i][front: back]
        # 0번째 배열에서 가져오는 값
        # ls[0][2:-1] = 0번 배열의 2번째 인덱스의 해당하는 값
        # 1번째 배열에서 가져오는 값
        # ls[1][1:-1] = 1번 배열의 2번째 인덱스와 해당 인덱스의 +1 -1의 위치에 해당하는 값

    elif i == cen:  # 만약 중심이 되는 인덱스부분일 경우 해당 인덱스의 모든 값을 추출
        result = ls[i]
    for e in result:  # 위에서 슬라이싱한 값들을 전부 total 더해가며 저장
        total += e

print(total)















