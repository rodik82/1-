w = input("Введите слово: ")
a=w.count("a")
e=w.count("e")
i=w.count("i")
o=w.count("o")
u=w.count("u")
print("В слове", w, a+e+i+o+u, "гласных и ", len(w)-a+e+i+o+u, "согластных")
if a==0:
    print("False")
elif e==0:
    print("False") 
elif i==0:
    print("False")
elif o==0:
    print("False")   
elif u==0:
    print("False")