import math
cell1 = input("Введите координаты начальной клетки: ")
cell2 = input("Введите координаты конечной клетки: ")
x1 = ord(cell1[0]) - ord('a')
y1 = int(cell1[1]) - 1
x2 = ord(cell2[0]) - ord('a')
y2 = int(cell2[1]) - 1
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("верно")
else:
    print("ошибка")