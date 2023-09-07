stroka = input("Введите строку: ")
l=len(stroka)
count=1
for i in range(l):
    if i==(l-1):
        print(stroka[i]+str(count),end='')
    else:
        if stroka[i]==stroka[i+1]:
            count=count+1
        else:
            print(stroka[i]+str(count),end='')
            count=1

