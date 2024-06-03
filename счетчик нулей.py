a = int(input("Введите количество чисел: "))
b = 0
for i in range (a):
    c = int(input("Введите число: ")) 
    if (c == 0):
        b += 1
print ("Вы ввели: ", b, "нулей")


