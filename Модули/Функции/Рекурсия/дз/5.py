import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def func_all(site):
    for _ in range(question):
        product = input('Введите название продукта для нового сайта: ').lower()
        print(f'Сайт для {product}:')
        site_copy = copy.deepcopy(site)
        site_copy['html']['head']['title'] = f'Куплю/продам {product} недорого'
        site_copy['html']['body']['h2'] = f'У нас самая низкая цена на {product}'
        func(site_copy)


def func(s, depth=0):
    for i in s:
        print(' ' * depth, i)
        if isinstance(s[i], dict):
            func(s[i], depth + 1)
        else:
            print(' ' * (depth + 1), ' '.join(s[i]))


question = int(input('\nСколько будет сайтов: '))
func_all(site)