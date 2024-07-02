a = int(input("ВВедите количество чисел первой строки и далее числа "))
tmp = set()
for i in range(a):
    n = input()
    tmp.add(n)
a1 = int(input("ВВедите количество чисел второй строки и далее числа "))
tmp1 = set()
for i in range(a1):
    n1 = input()
    tmp1.add(n1)
print ("Одинаковые числа -", len(tmp.intersection(tmp1)))
