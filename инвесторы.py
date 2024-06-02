x = int(input("Введите объем инвестиций: "))
a = int(input("Введите сколько долларов у Майкла: "))
b = int(input("Введите сколько долларов у Ивана: "))
if (a>=x) and (b>=x):
    print (2)
elif (a>=x) and (b<x):
    print ("Mike")
elif (a<x) and (b>=x):
    print ("Ivan")
elif (a<x) and (b<x) and (a+b==x):
    print(1)
else:
    print(0)

