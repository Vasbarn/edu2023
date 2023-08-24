x = int(input('Введите сумму вклада: '))
p = int(input('Введите процент: '))
y = int(input('Введите желаемую сумму: '))
years = 0
perc = 0
while x < y:
    x *= 1 + p / 100
    years += 1
print('Понадобится ', years, 'лет.')