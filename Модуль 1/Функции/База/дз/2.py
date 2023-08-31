def positive() -> None:
    print("Положительное")

def negative() -> None:
    print("Отрицательное")
def test(Num: int):
    if isinstance(Num, int):
        if Num > 0:
            positive()
        elif Num < 0:
            negative()


test()