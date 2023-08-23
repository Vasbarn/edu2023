import random
list = []
troika = 0
four = 0
five = 0
r = random.randint(3, 5)
N = int(input("Введите количество учеников: "))
for i in range(N):
    marks = random.randint(3, 5)
    list.append(marks)
for elem in range(0,N):
    if list[elem] == 3:
        troika += 1
    elif list[elem] == 4:
        four += 1
    else:
        five += 1
if  five < four > troika:
    print("Ударников больше")
elif four < five > troika:
    print("Отличников больше")
if five < troika > four:
    print("Троечников больше")
