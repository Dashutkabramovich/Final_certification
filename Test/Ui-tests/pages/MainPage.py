import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
      def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.chitai-gorod.ru/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

      with allure.step("Политика куки"):
           def set_cookie_policy(self): 
               cookie = {"name": "cookie_policy", "value": "1"}
               self._driver.add_cookie(cookie)

      with allure.step("Поиск книги на кириллице"):
           def rus_search(self,term):
               self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
               rus=self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
               return rus

      with allure.step("Поиск книги на латинице"):
          def eng_search(self,term):
              self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
              eng=self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
              return eng
    
      with allure.step("Пустой поиск"):
          def empty_search(self,term):
              self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
              empty=self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
              return empty
      
      with allure.step("Поиск по автору"):
          def author_search(self,term):
              self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
              author=self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
              return author
      
      with allure.step("Поиск сразу нескольких книг"):
            def books_search(self,term):
                self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
                two_books=self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
                return two_books
      
      with allure.step("Поиск по категории"):
          def series_search(self,term):
              self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
              series=self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
              return series
      
      with allure.step("Поиск через каталог"):
          def catalog_search(self):
              self._driver.find_element(By.XPATH, '//div[contains(text(),"Да, я здесь")]').click()
              self._driver.find_element(By.XPATH, '//span[contains(text(),"Каталог")]').click()
              self._driver.find_element(By.XPATH, '//span[contains(text(),"Художественная литература")]').click()
              catalog=self._driver.find_element(By.XPATH, '//span[contains(text(),"Поэзия")]').click()
              return catalog

      with allure.step("Просмотр акций на странице"):
           def promotions(self):
               self._driver.find_element(By.XPATH, '//div[contains(text(),"Да, я здесь")]').click()
               promo=self._driver.get("https://www.chitai-gorod.ru/promotions")
               return promo

      with allure.step("Проверка пустой корзины"):
            def get_empty_result_message(self):
                self._driver.get("https://www.chitai-gorod.ru/cart")
                txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[1]').text
                return txt
      
      with allure.step("Проверка фильтра 'Сначала новые'"):
            def filter_online(self,term): 
                self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
                self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
                self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div[1]/section/div[1]/div/div[1]/div').click()
                filter = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div[1]/section/div[1]/div/div[2]/div/div[2]').click()
                return filter
      
      with allure.step("Закрытие веб-браузера"):
            def close_driver(self):
                self._driver.quit()