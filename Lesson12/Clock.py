# 18. Создайте класс Clock, который имеет метод set_time(hours, minutes), но если
# передано невалидное время, оно устанавливается в 00:00

class Clock:

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def set_time(self, hours, minutes):
        if self.hours > 24 or self.minutes > 59:
            print("00:00")
        else:
            self.hours = hours
            self.minutes = minutes

    def __str__(self):
        return f"{self.hours:02} : {self.minutes:02}"

obj = Clock (22, 30)
print(obj)
obj1 = Clock(25,10)
print(obj1.set_time(25, 49))




