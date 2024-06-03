a = int(input("Введите число: "))
b = 0
for i in range (1,a+1):
    if (a%i==0):
        b += 1
        print(i, end=" ")
print ()
print ("Натуральных делителей числа: ", a, " : ", b)


