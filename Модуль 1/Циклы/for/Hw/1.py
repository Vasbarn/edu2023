import random
i = 0
Ubytok = 0
Dolzhniki=dict()
while i <= 10:
    nums = random.randint(-10,10)
    cred = random.randint (10000, 100000)
    if nums in Dolzhniki.keys():
        Dolzhniki[nums] += cred
    else:
        Dolzhniki[nums] = cred
    i += 1
    print(f"Id: {nums}, Sum: {cred}")
for i in Dolzhniki:
    if i < 0:
        Ubytok += Dolzhniki[i]

print(Dolzhniki)
print(f"Убыток составил {Ubytok} рублей")