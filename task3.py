n = int(input("Введите количество кварталов по горизонтали (N): "))
m = int(input("Введите количество кварталов по вертикали (M): "))
k = int(input("Введите количество кварталов для отделения (K): "))
if k == n or k == m or (n * m) % k == 0 :
    print("успешно")
else:
    print("неосуществимо")