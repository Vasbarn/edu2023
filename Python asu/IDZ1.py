from random import randint
import itertools
#1
from math import sqrt, floor

# A = int(input())
# while A > 103000:
#   print("Слишком большое число. Повторите ввод")
#   A = int(input())

# B =  floor(sqrt(A))
# print(B)

# 2
# N = int(input())
# while N < 1000 or N > 9999:
#   print("Слишком большое число. Повторите ввод")
#   N = int(input())

# thousand = N//1000
# hundred = (N % 1000) // 100
# dec = ((N % 1000) % 100) // 10
# un = N % 10
# print(thousand + hundred + dec + un, thousand*hundred*dec*un)

# 3
# s1 = str(input("Введите первую строку: "))
# s2 = str(input("Введите вторую строку: "))
#
# if sorted(s1) == sorted(s2):
#     print("Это слова анаграммы")
# else:
#     print("Это не анаграма")

#4
# coords = {}
# x_cord=[]
# y_cord=[]
# rad = []
# k = int(input("Количество грибов: "))
# t = int(input("Длительность дождя: "))
# for i in range(k):
#     X=randint(0,100)
#     Y=randint(0,100)
#     R = randint(1,10)
#     x_cord.append(X)
#     y_cord.append(Y)
#     rad.append(R)
#
# for el in range(0, len(x_cord)):
#     for _ in range(0,t):
#         if sqrt((x_cord[el+1]-x_cord[el])^2+(y_cord[el+1]-y_cord[el])^2) > (rad[el]+rad[el+1]):
#             rad[]
#
#
#5
# positive = []
# negative = []
# mylist = [randint(-10,10) for x in range(10)]
# for elem in mylist:
#     if elem < 0:
#         negative.append(elem)
#     else:
#         positive.append(elem)
#
# print(mylist)
# print(positive)
# print(negative)

#6
# sentence = str(input("Введите текст: "))
#
# words = sentence.split(' ')
# result = {}
# for word in words:
#     result[word] = result.get(word, 0) + 1
# print(result)

#7

# bundle1 = [randint(-10,10) for x in range(10)]
# bundle2= [randint(-10,10) for y in range(10)]
# nonr = []
# print(bundle1)
# print(bundle2)
# for elem1 in bundle1:
#     if not elem1 in nonr:
#         if elem1 in bundle1 and elem1 in bundle2:
#             nonr.append(elem1)
#     else:
#         continue
# print(nonr)

#8


