import allure
import requests
import pytest

base_url = "https://www.chitai-gorod.ru"

@allure.title("Поиск по одному слову")
@allure.description("Тест проверяет корректный поиск книги по одному слову")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_russian_lang():
    with allure.step("api. Поиск по одному слову через API"):
        resp = requests.get(base_url+'/search?phrase=гарри')
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "text/html; charset=utf-8"

@allure.title("Поиск по нескольким словам")
@allure.description("Тест проверяет корректный поиск книги по нескольким словам")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_russian_lang_two_words():
    with allure.step("api. Поиск по нескольким словам через API"):
        resp = requests.get(base_url+'/search?phrase=гарри поттер')
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "text/html; charset=utf-8"

@allure.title("Поиск по автору")
@allure.description("Тест проверяет корректный поиск книги по автору")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_author():
    with allure.step("api. Поиск по автору через API"):
        resp = requests.get(base_url+'/search?phrase=Джоан Роулинг')
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "text/html; charset=utf-8"

@allure.title("Поиск по серии")
@allure.description("Тест проверяет корректный поиск книги по серии")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_series():
    with allure.step("api. Поиск по серии через API"):
        resp = requests.get(base_url+'/search?phrase=Дозоры')
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "text/html; charset=utf-8"

@allure.title("Поиск по жанру")
@allure.description("Тест проверяет корректный поиск книги по жанру")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_genre():
    with allure.step("api. Поиск по жанру через API"):
        resp = requests.get(base_url+'/search?phrase=Любовный роман')
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "text/html; charset=utf-8"

@allure.title("Поиск по латинице")
@allure.description("Тест проверяет корректный поиск книги на английском")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_eng():
    with allure.step("api. Поиск на латинице через API"):
        resp = requests.get(base_url+'/search?phrase=Harry Potter')
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "text/html; charset=utf-8"

@allure.title("Поиск канцелярии")
@allure.description("Тест проверяет корректный поиск сопутствующих товаров на сайте")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_alt_products():
    with allure.step("api. Поиск сопутствующих товаров через API"):
        resp = requests.get(base_url+'/search?phrase=Канцелярия')
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "text/html; charset=utf-8"

@allure.title("Негативная проверка поиска с DELETE")
@allure.description("Отправка запроса поиска с канцелярии с неверным методом DELETE")
@allure.feature("DELETE")
@allure.severity("trivial")
@pytest.mark.negative_test
def test_alt_products_del():
    with allure.step("api. Отправка запроса поиска с неверным методом DELETE через API"):
        resp = requests.delete(base_url+'/search?phrase=Канцелярия')
        assert resp.headers["Content-Type"] == "text/html; charset=utf-8" 
        if resp.status_code == 200:
            print('Success')  
        elif resp.status_code == 404:
            print('Not Found')

@allure.title("Негативная проверка ввода в поиск иероглифов")
@allure.description("Тест проверяет, что сайт выдаёт ошибку при вводе невалидных символов")
@allure.feature("READ")
@allure.severity("minor")
@pytest.mark.negative_test
def test_hieroglyphs():
    with allure.step("api. Отправка запроса с иероглифами через API"):
        resp = requests.get(base_url+'/search?phrase=ᯓᡣ𐭩𐙚˚‧ ୨୧')
        assert resp.headers["Content-Type"] == "text/html; charset=utf-8"
        assert 'Похоже, у&nbsp;нас такого нет' in resp.text 

@allure.title("Негативная проверка ввода в поиск знаков препинания")
@allure.description("Тест проверяет, что сайт выдаёт ошибку при вводе знаков препинания")
@allure.feature("READ")
@allure.severity("minor")
@pytest.mark.negative_test
def test_coma():
    with allure.step("api. Отправка запроса со знаками препинания через API"):
        resp = requests.get(base_url+'/search?phrase=!.,.?')
        assert resp.headers["Content-Type"] == "text/html; charset=utf-8"
        assert 'Похоже, у&nbsp;нас такого нет' in resp.text 

@allure.title("Пустой поиск")
@allure.description("Тест проверяет отображение сообщения 'Похоже, у нас такого нет' при пустом поиске")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.negative_test
def test_empty():
    with allure.step("api. Отправка пустого поиска с возвращением о получении сообщений 'Вы ввели пустой запрос' или'У нас такого нет'через API"):
        resp = requests.get(base_url+'/search?phrase=')
        assert resp.headers["Content-Type"] == "text/html; charset=utf-8"
        if 'Вы, ввели&nbsp;пустой запрос' in resp.text:
            print('Success')  
        elif 'Похоже, у&nbsp;нас такого нет' in resp.text:
            print('Неверный ответ')