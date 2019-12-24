import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
ls = []
count = 0
for _ in range(n) :
    lss = list(map(int,input().split()))
    ls.append(lss)
ls.insert(0, [0]*(n+2))
ls.append([0]*(n+2))
for i in range(1,len(ls)-1) :
    ls[i].insert(0,0)
    ls[i].append(0)

for i in range(1,len(ls)-1) :
    for j in range(1,len(ls)-1) :
        up = ls[i-1][j]
        down = ls[i+1][j]
        right = ls[i][j+1]
        left = ls[i][j-1]
        if ls[i][j] > up and ls[i][j] > down and ls[i][j] > right and ls[i][j] > left :
            count =count +1
print(count)