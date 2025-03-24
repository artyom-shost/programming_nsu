n = int(input("Введите количество детей (N): "))
k = int(input("Введите вместимость карусели (K): "))
m = int(input("Введите длительность сеанса (M): "))
rides = (n * 2 + k - 1) // k
total_time = rides * m
print(total_time)