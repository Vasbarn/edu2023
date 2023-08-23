N = int(input("Введите число: "))
cards = 0
exist_cards = 0
for i in range(1, N):
    cards += i
for j in range(1,N-1):
    exist_cards += j
last_card = cards - exist_cards
print(last_card)

