Итоговый проект по курсу -- Автоматизация тестирования с помощью Selenium и Python

Тестирование онлайн магазина: http://selenium1py.pythonanywhere.com/

Реализованы следующие тесты:

Добавление товара в корзину гостем
Добавление товара в корзину зарегистрированным пользователем
Переход на страницу логина
Проверка корзины без товаров
Тесты написаны с использованием шаблона Page Object

Работаю с драйвером для Chrome.

Тестирование организованно с помощью:

Python 3.7.3
Система управления пакетами pip
Бибилиотека Selenium 3.14.0
Драйвер для Chrome ChromeDriver
unittest
PyTest 5.1.1
Linux

Установка системы управления пакетами pip:
```
$ sudo apt-get install -y python3-pip
```
Установка библиотеки Selenium:
```
pip install selenium==3.14.0
pip list
```
Установка ChromeDriver версии 77:
```
$ wget https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip
```
Другую версию chromedriver для браузера Chrome можно скачать по следующей ссылке https://sites.google.com/a/chromium.org/chromedriver/downloads.

Переместите разархивированный файл с СhromeDriver в нужную папку и разрешите запускать chromedriver как исполняемый файл:
```
$ sudo mv chromedriver /usr/bin/chromedriver
$ sudo chown root:root /usr/bin/chromedriver
$ sudo chmod +x /usr/bin/chromedriver
```
Установка PyTest:
```
$ pip install pytest==5.1.1
```
Для запуска тестов используйте команды:
```
pytest -s test_main_page.py
pytest -s test_product_page.py
```
Для запуска с другим языком используйте комнду, где вместо es может быть указан нужный вам язык:
```
pytest --language=es test_main_page.py 
```
Для запуска тестов отмаркированных @pytest.mark.need_review выполните команду:
```
pytest -v --tb=line --language=en -m need_review
```
