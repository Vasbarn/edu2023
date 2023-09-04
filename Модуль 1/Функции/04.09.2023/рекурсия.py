

def simple_func(num: int = 10) -> None:
	for elem in range(1, num + 1):
		print(elem)


# simple_func()

list_result = list()


def req_func(num: int = 10, counter: int = 1, list_result: list = None) -> list:
	if counter > num:
		return list_result
	list_result.append(counter)
	counter = counter + 1
	req_func(num=num, counter=counter, list_result=list_result)


print(req_func(list_result=list_result))
print(list_result)



