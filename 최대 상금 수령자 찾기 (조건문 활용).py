# 규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
# 규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
# 규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.

# 주사위 3개와 위와 같은 규칙이 주어 질 때 각 규칙에 맞는 상금 중 가장 큰 상금을 출력하라

mss = []
n = int(input())
for i in range(n):
    money = 0
    ls = list(map(int, input().split()))
    ls.sort(reverse=True)
    if ls[0] == ls[1] and ls[1] == ls[2]:
        money = 10000 + ls[0] * 1000

    elif ls[0] == ls[1] or ls[0] == ls[2]:
        money = 1000 + ls[0] * 100

    elif ls[1] == ls[2]:
        money = 1000 + ls[1] * 100

    elif ls[0] != ls[1] and ls[1] != ls[2]:
        money = ls[0] * 100
    mss.append(money)
mss.sort(reverse=True)
print(mss[0])




