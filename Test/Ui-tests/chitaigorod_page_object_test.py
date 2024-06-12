import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage

@allure.title("Открытие сайта")
@allure.description("Тест проверяет наличие связи с сайтом")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_chitay_gorod(): 
    with allure.step("Открытие веб-страницы Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser) 
        main_page.set_cookie_policy() 

@allure.title("Поиск на кириллице")
@allure.description("Тест проверяет поиск книги на русском языке")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_rus_search():
    with allure.step("Открытие веб-страницы Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        main_page.rus_search('Капитанская дочка')

@allure.title("Поиск на латинице")
@allure.description("Тест проверяет поиск книги на английском языке")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_eng_search():
    with allure.step("Открытие веб-страницы Chrome и выполнение поиска"):
         browser = webdriver.Chrome()
         main_page = MainPage(browser) 
         main_page.set_cookie_policy()
         main_page.eng_search('Harry Potter and the philosoprhers stone') 

@allure.title("Пустой поиск")
@allure.description("Тест проверяет вылонение пустого поиска")
@allure.feature("READ")
@allure.severity("trivial")
@pytest.mark.negative_test 
def test_empty_search():
    with allure.step("Открытие веб-страницы Chrome и выполнение поиска"):
         browser = webdriver.Chrome()
         main_page = MainPage(browser) 
         main_page.set_cookie_policy()
         main_page.empty_search('no book search term') 

@allure.title("Поиск по автору")
@allure.description("Тест проверяет корректное выполнение поиска по автору")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_author_search():
    with allure.step("Открытие веб-страницы Chrome и выполнение поиска"):
         browser = webdriver.Chrome()
         main_page = MainPage(browser) 
         main_page.set_cookie_policy()
         main_page.author_search('Шекспир') 

@allure.title("Поиск по двум книгам")
@allure.description("Тест проверяет корректное выполнение поиска сразу по нескольким книгам")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_books_search():
    with allure.step("Открытие веб-страницы Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        main_page.books_search('Бесприданница, Золушка') 

@allure.title("Поиск по категории")
@allure.description("Тест проверяет корректное выполнение поиска по категории книг")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_series_search():
    with allure.step("Открытие веб-страницы Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        main_page.series_search('Книги для детей') 

@allure.title("Просмотр акций")
@allure.description("Тест проверяет открытие страницы с промоакциями")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.positive_test
def test_promo():
    with allure.step("Открытие веб-страницы Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        main_page.promotions()

@allure.title("Поиск по каталогу")
@allure.description("Тест проверяет корректное выполнение поиска, используя каталог")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.positive_test
def test_catalog_search():
    with allure.step("Открытие веб-страницы Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        main_page.catalog_search() 

@allure.title("Поиск по фильтру")
@allure.description("Тест проверяет корректное выполнение поиска, используя фильтр")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.positive_test
def test_filter_online():
   with allure.step("Открытие веб-страницы Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser)
        main_page.set_cookie_policy() 
        main_page.rus_search('Айвенго')
   with allure.step("Проверка фильтра'Сначала новые'"):
        main_page.filter_online('') 
        
@allure.title("Проверка пустой корзины")
@allure.description("Тест проверяет, что в пустой корзине воникает сообщение 'В корзине ничего нет'")
@allure.feature("")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_get_empty_result_message():
    with allure.step("Открытие веб-страницы Chrome"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser)
        main_page.set_cookie_policy() 
    with allure.step("Проверка пустой корзины с сообщением 'В корзине ничего нет'"):
        msg = main_page.get_empty_result_message()
        assert msg == "В корзине ничего нет"
    with allure.step("Зактытие браузера"):
        main_page.close_driver()