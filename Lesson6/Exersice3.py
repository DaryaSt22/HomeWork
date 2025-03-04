# Является ли число простым
a = int(input())
if a == 1:
    print("Число не является простым")
else:
    devisors = 0
    for i in range(1, a + 1):
        #print(i)
        if a % i == 0:
            devisors += 1
    if devisors == 2:
        print("Число простое")
    else:
        print("Число не является простым")
