import random
def pl (t):
    for i in t:
        print (*i)
x = int(input("Число строк "))
y = int(input("Число столбцов "))
mat1 = [[random.randint(1, 11) for j in range(y)] for i in range(x)]
mat2 = [[random.randint(1, 11) for j in range(y)] for i in range(x)]
mat3 = [[random.randint(1, 11) for j in range(y)] for i in range(x)]
for i in range(x):
    for q in range(y):
        mat3[i][q] = mat1[i][q] + mat2[i][q]
print ("Первая матрица")
pl (mat1)
print ("Вторая матрица")
pl (mat2)
print ("Результат сложения")
pl (mat3)