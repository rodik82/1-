a = int(input("ВВедите количество чисел "))
tmp = set()
for i in range(a):
    n = input()
    tmp.add(n)
print ("Вы ввели", len(tmp), "различных чисел")
