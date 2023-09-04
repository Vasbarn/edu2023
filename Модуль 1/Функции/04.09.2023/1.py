def pyramid(num: int, sym: str) -> None:
    for i in range(1, num + 1):
        print(sym * i)


pyramid(5, str(1))
