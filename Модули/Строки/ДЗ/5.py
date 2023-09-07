password = input("Введите пароль: ")
count=0
bukva=0
for i in password:
    if i.isdigit()==True:
        count+=1
    if i.isupper()==True:
        bukva+=1

if len(password) >= 8 and bukva >= 1 and count >= 3:
    print("Это надежный пароль")
else:
    print("Это ненадежный пароль. Повторите ввод")