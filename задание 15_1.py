class Transport(object):
    name = "Reno"
    max_speed = 150
    mileage = 10

    def __init__(self, n, s, m):
        self.name = n
        self.max_speed = s
        self.mileage = m

autobus = Transport ("Renault Logan", 180, 12)
print (f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")
        
        

