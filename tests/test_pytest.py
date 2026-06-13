def test_first_try():
    print("Hello World!")


def test_assert_positive_case():  # которые проверяет положительный кейс
    assert (2 + 2) == 4  # Ожидается, что тест пройдет


def test_assert_negative_case():  # проверяет негативный кейс
    assert (2 + 2) == 5  # Тут должна быть ошибка
