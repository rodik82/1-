n = [int(s) for s in input().split()]
tem = set()
for num in n:
    if num in tem:
        print('YES')
    else:
        print('NO')
        tem.add(num)