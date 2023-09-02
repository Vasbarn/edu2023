


def get_dict() -> list:
	my_dict = list()
	return my_dict


def test(x: int, y: str, *args, **kwargs) -> dict:
	result = 0
	for i in args:
		if isinstance(i, int):
			result += i
		elif isinstance(i, str):
			print(i)
	print(result)
	print("А имя мне - {}".format(kwargs.get("name")))
	print(x, y)
	return dict()


test(1, "2", 3, "ЫВ", 1, name="Саша")


