# 숫자가 큰 순서대로 나눌수 있을만큼 나누고 몫을 저장한다
n = int(input())

for j in range(n):
    money = int(input())
    for i in [25, 10, 5, 1]:
        print(money // i, end=' ')
        money = money % i