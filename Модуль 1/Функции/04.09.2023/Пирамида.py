def piramida(num: int, symbol: str) -> None:
	num_popolam = num // 2
	for numer in range(1, num + 1):
		num_popolam -= 1
		print(((" " * (num_popolam-numer)) + (symbol * numer)))


piramida(10, "|")

