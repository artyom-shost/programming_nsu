cell = input("Введите координаты клетки шахматного поля: ")
x = ord(cell[0]) - ord('a')
y = int(cell[1]) - 1
if (x + y) % 2 == 0:
    print("черная")
else:
    print("белая")