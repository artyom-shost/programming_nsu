a = float(input("Введите высоту отверстия: "))
b = float(input("Введите ширину отверстия: "))
c = float(input("Введите введите длину кирпича: "))
d = float(input("Введите введите ширину кирпича: "))
e = float(input("Введите введите высоту кирпича: "))
if ((a >= c and b >= d) or (a >= d and b >= c) or (a >= d and b >= e) or (a >= e and b >= d) or (a >= c and b >= e) or (a >= e and b >= c)):
    print("да")
else:
    print("нет")