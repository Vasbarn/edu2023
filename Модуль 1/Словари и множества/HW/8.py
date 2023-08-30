text = input("Введите текст: ")
slova = set()
for i in text:
    if i not in slova:
        slova.add(i)
    else:
        slova.remove(i)
if len(slova) < 1:
    print("Можно составить палиндром")
else:
    print("Нельзя составить палиндром")