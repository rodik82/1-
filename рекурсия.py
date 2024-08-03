def pl (t):
    if t < 0:
        return
    pl (t - 1)
    print (t)
n = int(input())
pl(n)
print ("Конец списка")
