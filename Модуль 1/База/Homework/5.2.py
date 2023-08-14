a = int(input("Введите четырехзначное число: "))
thousand = a//1000
hundred = (a%1000)//100
desyatki =(a%100)//10
last_count = a%10
print(thousand,hundred,desyatki,last_count, sep="\n")
