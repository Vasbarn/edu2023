import random
Dolzhniki = int(input("Количество должников: "))
total = 0
for i in range(0,Dolzhniki, 5):
    r = random.randint(1000, 500000)
    print(f"Сумма долга составляет {r} рублей")
    total += r
print("Общая сумма долга:", total)
