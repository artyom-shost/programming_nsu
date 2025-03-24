n = int(input("Введите порядковый номер цифры: "))

if n == 0:
    result = 1
else:
    result = (n + n // 10 + 1)

print(result)
