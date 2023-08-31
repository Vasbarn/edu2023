def summa(x):
    if type(x) is str:
        print("Это строка")
    elif type(x) is list:
        return
    else:
        raise TypeError


print (summa(("mir", "privet")))



