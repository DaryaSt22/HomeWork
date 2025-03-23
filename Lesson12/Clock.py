# 18. Создайте класс Clock, который имеет метод set_time(hours, minutes), но если
# передано невалидное время, оно устанавливается в 00:00

class Clock:

    def set_time(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes


