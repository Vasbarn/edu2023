first_quartal = int(input("Введите доход за первый квартал: "))
sec_quartal = int(input("Введите доход за второй квартал: "))
pre_last_quartal = int(input("Введите доход за предпоследний квартал: "))
last_quartal = int(input("Введите доход за последний квартал: "))
sum_first = first_quartal+sec_quartal
sum_last = pre_last_quartal+last_quartal
print("Коэффициент динамики:",sum_first/sum_last)