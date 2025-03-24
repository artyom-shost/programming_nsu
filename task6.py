n = int(input("Введите количество детей (N): "))
k = int(input("Введите вместимость карусели (K): "))
m = int(input("Введите длительность сеанса (M): "))
if n <= k:
    total_time = m * 2
else:
    rides = (n * 2 + k - 1) // k
    total_time = rides * m
print(total_time)
