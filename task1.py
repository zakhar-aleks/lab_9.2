a = int(input("Введіть кількість учнів у першому класі: "))
b = int(input("Введіть кількість учнів у другому класі: "))
c = int(input("Введіть кількість учнів у третьому класі: "))

desks_a = a // 2 + a % 2
desks_b = b // 2 + b % 2
desks_c = c // 2 + c % 2

print(f"Результат: {desks_a + desks_b + desks_c}")