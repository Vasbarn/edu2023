array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
list_1=[]
for i in array_1:
    if i in (array_2 and array_3):
        list_1.append(i)
print("Числа во всех списках(безмножественный способ):", list_1)

a = set(array_1)
b = set(array_2)
c = set(array_3)
print("Числа во всех списках(множественный способ):", a & b & c)

list_2=[]
for i in array_1:
    if  i  not in (array_2 or array_3):
        list_2.append(i)
print("Числа в 1 списке(безмножественный способ):",list_2)

a = set(array_1)
b = set(array_2)
c = set(array_3)
print("Числа в 1 списке(множественный способ):",a - b - c)










