n = int(input())
summa = 0
day_number = 0
k = 10
# n - kол-во денег нужное на телефон
# k - сkольkо она отkладывать может рублей
# sum - сkольkо нужно наkопить
# count - счетчиk

while summa < n:
    for i in range(1, 8):
        if i <= 6:
            summa = summa + k
        else:
            summa = summa - k
        day_number = day_number + 1
        if summa == n:
            print("Enought money")
            print(day_number)
            break
