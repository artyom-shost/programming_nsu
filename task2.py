import math
a = float(input("Введите высоту отверстия: "))
b = float(input("Введите ширину отверстия: "))
c = float(input("Введите введите длину кирпича: "))
d = float(input("Введите введите ширину кирпича: "))
e = float(input("Введите введите высоту кирпича: "))
if (math.sqrt(a ** 2 + b ** 2) >= math.sqrt(c ** 2 + d ** 2)) or (math.sqrt(a ** 2 + b ** 2) >= math.sqrt(c ** 2 + e ** 2)) or (math.sqrt(a ** 2 + b ** 2) >= math.sqrt(d ** 2 + e ** 2)):
    print("да")
else:
    print("нет")
