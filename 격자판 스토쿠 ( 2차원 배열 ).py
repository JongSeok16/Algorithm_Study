import sys
# sys.stdin =open("input.txt", "rt")
ls= []
count = 0
for _ in range(9) :
    lss = list(map(int, input().split()))
    ls.append(lss)


def call (ls) :
    tt = 0
    st = 0
    bc = 3
    c = 0
    for i in range(9) :
        tt1 = 0
        tt2 = 0
        for j in range(9) :
            tt1 = tt1 + ls[i][j]
            tt2 = tt2 + ls[j][i]
        if tt1 != 45 or tt2 != 45 :
            print("NO")
            return False
    for i in range(3) :
        for j in range(9) :
            tt = tt + sum(ls[j][st:bc])
            c = c + 1
            if c == 3 :
                if tt != 45 :
                    print("NO")
                    return False
                else:
                    c = 0
                    tt = 0
        st = st +3
        bc = bc +3
    print("YES")
    return True
call(ls)




