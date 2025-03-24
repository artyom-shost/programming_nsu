import math
arena_radius = 6.5
carpet_a = float(input("Введите длину ковровой дорожки (в метрах): "))
carpet_b = float(input("Введите ширину ковровой дорожки (в метрах): "))
carpet_diagonal = math.sqrt(carpet_a**2 + carpet_b**2)
if carpet_diagonal <= arena_radius * 2:
    print("да")
else:
    print("нет")