class kassa(object):
    v_kasse = 2000
    top_up = 1000 
    zabrat = 1000

    def __init__(self, n, s, m):
       self.v_kasse = n
       self.top_up = s
       self.zabrat = m

    def dol(self):
        self.v_kasse += self.top_up 
        print(f'После покупки в кассе {k1.v_kasse}')

    def count_1000(self):
        print(f'После покупки в кассе {k1.v_kasse//1000} целых тысячи')

    def ost(self):
        if self.v_kasse - self.zabrat >= 0:
            self.v_kasse -= self.zabrat
            print(f'Вы забрали {k1.zabrat}, в кассе осталось {k1.v_kasse}')
        else: 
            print(f"Не достаточно денег в кассе")     
            

k1 = kassa(4000, 1500, 5000)
k1.dol() 
k1.count_1000()
k1.ost()
