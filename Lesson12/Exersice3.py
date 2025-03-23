# Класс «Автобус». Класс содержит свойства:
# ● скорость
# ● максимальное количество посадочных мест
# ● максимальная скорость
# ● список фамилий пассажиров
# ● флаг наличия свободных мест
# ● словарь мест в автобусе

class Bus:
    def __init__(self, max_seat, max_speed):
        self.speed = 0
        self.max_seat = max_seat
        self.max_speed = max_speed
        # self.surname_passengers = surname_passengers
        # self.flag_vacant_seat = flag_vacant_seat
        self.dictionary_vacant_seat = {} # {место: фамилия}

    # Метод - посадка и высадка одного или нескольких пассажиров


    # Метод - увеличение и уменьшение скорости на заданное значение


    # Метод - операции in, += и -= (посадка и высадка пассажира по фамилии)




