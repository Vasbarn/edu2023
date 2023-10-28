def get_rating(url: str, adres: str, listing: list) -> list:
    response = requests.get(url, headers=header).text
    soup = BeautifulSoup(response, "lxml")
    main = soup.find(class_ = "business-header-rating-view__user-rating")
    # for m in main:
    #     rate = m.find(class_ = "business-rating-badge-view__rating-text _size_m").text
    #     calls = m.find(class_ = "business-header-rating-view__text _clickable").text
    #     print(rate)
    #     print(calls)
    # contains = main.find(class_="_y10azs")
    # contains2 = main.find(class_="_jspzdm")
    # diction = {}
    # diction["Количество отзывов"] = contains2.text
    # diction["Рейтинг"] = contains.text
    # diction["Название магазина"] = adres
    # listing.append(diction)
