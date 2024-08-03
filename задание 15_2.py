class Transport(object):
    name = "Reno"
    max_speed = 150
    mileage = 10
    seating_capacity = 50

    def __init__(self, n, s, m, c):
       self.name = n
       self.max_speed = s
       self.mileage = m
       self.seating_capacity = c

autobus = Transport ("Renault Logan", 180, 12, 50)
print (f"Вместимость одного автобуса {autobus.name}: {autobus.seating_capacity} пассажиров")
        
        

