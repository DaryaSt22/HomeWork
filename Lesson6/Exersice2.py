num = int(input())
print(bin(num))


def num2Bin(n):
    if n == 0:
        return
    num2Bin(n // 2)
    print(n % 2, end="")
print(num2Bin(6))