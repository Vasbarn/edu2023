# for x in range(10):
#     print(x, end=" ")
# print()
# for x in range(5, 10):
#     print(x, end=" ")
# print()
# for x in range(0, 10, 2):
#     print(x, end=" ")
list1 = ["Это2", "список2", "!2"]
list2 = ["Это3", "список3", "!3"]
list3 = ["Это4", "список4", "!4"]
x = "список2"

for idx, elem in enumerate([list1, list2,  list3]):
    if elem.count(x) > 0:
        print("В списке под {} элементом содержится искомое значение {}".format(idx + 1, x))
        break
else:
    print("Цикл отработал без break'ов")
print("Этот код будет выполнен всегда")
