import random
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
            },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
            }
    }
}
def search(slovar: dict, key: str, depth: int, m_depth: int):
    if key in slovar:
        return slovar[key]
    if depth > 1:
        for val in slovar.values():
            if isinstance(val, dict):
                result = search(val, key, depth - 1, m_depth)
            if result:
                break
            else:
                result = None
    return result


user_key = input("Какой ключ ищем? ")
max_depth = input("Хотите ввести максимальную глубину? Y/N:").lower()

if max_depth == "y":
    search_depth = int(input("Введите максимальную глубину: "))
    value = search(site, user_key, search_depth, max_depth)
    print("Значение ключа: ", value)
elif max_depth == "n":
    search_depth = random.randint(1, 10)
    value = search(site, user_key, search_depth, max_depth)
    print("Значение ключа: ", value)