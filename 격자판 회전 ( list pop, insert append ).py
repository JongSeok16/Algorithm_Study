import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
ls = []
for _ in range(n) :
    lss = list(map(int, input().split()))
    ls.append(lss)
n = int(input())
for _ in range(n):
    index_n, dc, mv = map(int, input().split())
    for i in range(mv) :
        if dc == 0:
            ls[index_n-1].append(ls[index_n-1][0]) # 0
            ls[index_n-1].pop(0)
        elif dc != 0:
            ls[index_n-1].insert(0, ls[index_n-1][-1])
            ls[index_n-1].pop(-1)

n = len(ls)
s = 0
e = 0
total = 0
cen = n // 2
for i in range(n) :
    if i == 0 or i == n-1 :
        total += sum(ls[i])
    elif i <= cen :
        s += 1
        e -= 1
        total += sum(ls[i][s:e])
    elif i > cen :
        s -= 1
        e += 1
        total += sum(ls[i][s:e])
print(total)
