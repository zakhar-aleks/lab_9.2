count = 0

prev = int(input("Введіть число: "))

if prev != 0:
    while True:
        curr = int(input("Введіть число: "))
        
        if curr == 0:
            break

        if curr > prev:
            count += 1

        prev = curr

print(count)