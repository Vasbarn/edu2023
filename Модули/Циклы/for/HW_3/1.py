slovar = []
for _ in range(10):
    word = input("Введите слово: ").lower()
    slovar.append(word)
print(f"В пираты завербовано {slovar.count('карамба')} человек")

