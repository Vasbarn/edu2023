def print_it(my_str: str, counter: int = 1, mode: str = 3, ) -> str:
	my_str *= counter
	if mode == "1":
		return my_str.upper()
	elif mode == "2":
		return my_str.lower()
	elif mode == "3":
		return my_str


def print_it2(*args) -> str:
	my_str, counter, mode = args
	my_str *= counter
	if mode == "1":
		return my_str.upper()
	elif mode == "2":
		return my_str.lower()
	elif mode == "3":
		return my_str

# my_string6 = print_it2("Привет мир!", 1, "1")
# print(my_string6)


def print_it3(**kwargs) -> str:
	my_str, counter, mode = kwargs.get("my_str"), kwargs.get("counter"), kwargs.get("mode"),
	my_str *= counter
	if mode == "1":
		return my_str.upper()
	elif mode == "2":
		return my_str.lower()
	elif mode == "3":
		return my_str


my_string6 = print_it3(my_str="Привет мир!", counter=1, mode="1")
print(my_string6)


