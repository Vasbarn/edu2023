for i in range(10, 100): 
    list = (i // 10) * (i % 10) * 3
    if list == i:
        print(i)