# input 값으로 두 개의 자연수 N과 K가 주어졌을 때,
# N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성


n = input()
a, b = map(int, n.split())

count = 0 # 약수가 들어올 때 마다 카운트

for i in range(1, a+1) :
    if a % i == 0 :
        count += 1
    if count == b :
        print(i)
        break

else : # 약수의 수 보다 입력값이 클 경우 -1
    print(-1)