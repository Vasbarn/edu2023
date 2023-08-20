ip_add = input("Введите IP-адрес: ").split('.')
if len(ip_add)<4:
    print("IP-адрес неверный")
else:
    for i in ip_add:
        if int(i) >= 0 and int(i) <= 255 and i.isdigit()==True:
            print("IP-адрес верный")
            break
        else:
            print("IP-адрес неверный")
            break
