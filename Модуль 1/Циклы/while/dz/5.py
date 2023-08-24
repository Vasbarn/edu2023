plan = 0
i = 1
call = 0
while i <= 8:
    print( i, "час работы")
    task = int(input("Сколько задач решит Максим?"))
    plan += task
    call = int(input("Звонит жена, взять трубку? (1 - если да, 0 - если нет) "))
    i += 1
print(f"Количество выполненных задач: {plan}")
if call == 1:
    print("Нужно в магазин")