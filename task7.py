k = int(input("Введите количество суши: "))

possible = False
for num_7 in range(k // 7 + 1):
    k1 = k - num_7 * 7
    if k1 >= 0 and k1 % 5 == 0:
        possible = True
        break

if possible:
    print("да")
else:
    print("нет")