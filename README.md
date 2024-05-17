# Autotest
Этот скрипт предназначен для автоматизации тестирования на примере приложения для списка дел, доступного по следующему URL: https://lambdatest.github.io/sample-todo-app/.

## Требования
Python 3.x
Библиотека Selenium
Драйвер Edge WebDriver

## Установка
Убедитесь, что у вас установлен Python на вашей системе. Вы можете загрузить его с python.org.
Установите библиотеку Selenium, запустив команду pip install selenium.

## Использование
Откройте терминал или командную строку.
Перейдите в каталог, где сохранен скрипт.
Запустите скрипт с помощью команды python имя_скрипта.py.

## Описание
Этот скрипт автоматизирует следующие действия в приложении списка дел:

- Проверяет, что изначальное количество оставшихся задач указано правильно.
- Отмечает первую задачу как выполненную и проверяет изменение.
- Добавляет новый элемент в список и отмечает его как выполненный.

## Примечания
Убедитесь, что драйвер Edge WebDriver правильно установлен и настроен перед запуском скрипта.
Убедитесь, что URL, указанный в скрипте, доступен, и приложение для списка дел работает корректно.