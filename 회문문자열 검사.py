# N개의 문자열 데이터를 입력받아
# 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면
# YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
# 단 회문을 검사할 때 대소문자를 구분하지 않습니다.

# 5
# level
# moon
# abcba
# soon
# gooG

# 위의 문제는 해당 문자열을 받아서
# level의 경우 0,1,2,3,4 의 인덱스가 있을 때
# 0 -> 4, 4 -> 0 으로 바꾸어주면서 비교해주면 되는 문제

n = int(input())
a = []
for i in range(n) :
    count = 0
    strs = str(input())
    strs = strs.upper() # 모든 문자열을 대문자로 바꾸어줌
    ns = len(strs)
    nss = 0 # 비교할 횟수
    if ns % 2 == 0 : # 주어진 문자열의 크기가 짝수일 경우
        nss = len(strs) // 2 # 무어진 문자열의 크기 / 2 의 몫을 값 할당
    elif ns % 2 == 1 : # 주어진 문자열의 크기가 홀수일 경우
        nss = (len(strs) -1) // 2 # 주어진 문자열의 크기 -1을 한 값에 /2를 한 몫을 할당

    for j in range(ns) : # 입력받은 문자열의 크기만큼 for 루프 실행
        if strs[j] == strs[-1-j] :
            count += 1
            # strs = level의 경우 j가 0이라고 가정한다면
            # srts[j] = l, srts[-1-j] = l

            # strs = level의 경우 j가 1이라고 가정한다면
            # srts[j] = e, srts[-1-j] = e
        if count == ns :
            a.append("YES")

        elif strs[j] != strs[-1-j] :
            a.append("NO")
            # 앞과 뒤의 문자가 같지 않다면 해당 반복문 탈출
            break
print(a)