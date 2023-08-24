second = int(input('Введите количество секунд:'))
for i in range (second,-1, -1):
    print ('Количество секунд: ', i)
    if i == 0:
        print("Ваша еда готова, осторожно горячo!")
    reverse_timer = int(input('Остановить разогрев? '))
    if reverse_timer == 1:
        print ('Ваша еда готова, можно забрать ', i)
        break
