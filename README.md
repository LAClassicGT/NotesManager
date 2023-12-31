## Описание проекта
__Приложение представляет собой менеджер заметок, где пользователь может создавать, хранить, искать и удалять заметки. Для хранения данных будет использоваться база данных__ **SQLite**.


## Основная функциональность:

### Добавление новой заметки:
- __Пользователь может добавить новую заметку, указав заголовок и содержание__.
- __Заметка должна быть сохранена в базе данных__.
### Просмотр списка всех заметок:
- __Приложение должно отображать список всех заметок с их заголовками__.
- __Пользователь может выбрать заметку из списка для просмотра подробной информации__.

### Поиск заметки:
- __Пользователь может ввести ключевое слово или фразу для поиска__.
- __Приложение должно отобразить список заметок, содержащих данное ключевое слово__.

### Удаление заметки:
- __Пользователь может выбрать заметку из списка и удалить её__.
- __Заметка должна быть удалена из базы данных__.

## Инструкция для запуска консольного приложения:

## Установка Python и пакетов:

- __Переход по ссылке на страницу установки Python: www.python.org/downloads/__.
- __Установка пакета colorama: `pip install colorama`__.

## Установка проекта NotesManager:

### Установка:
- __Установка происходит прямо с этого репозитория__.
- __После установки запустите главный файл main.py__.
- __Дождитесь конца загрузки прогресс-бара__.

### Файловый менеджер:
- __`README`: инструкция, документация, обьяснение__.
- __`main.py`: Исполнительный файл, главный файл__.
- __`NotesManager/NotesManager.py`: Файл для связи, модуль__.
- __`DataBase/DataBase.py`: Файл для связи с базой данных__.
- __`DataBase/db/notes.db`: Файл, который является носителем входных данных, база данных__.

## Меню приложения:

- __"Создать заметку": Создает заметку, с названием и содержанием, которое вы укажите при создании__.
- __"Показать список заметок": Показывает список всех заметок и их ID, которые вы создали ранее, так же выводит содержимое выбранной заметки__.
- __"Показать список заметок по ключевому слову": Показывает список заметок, которые удалось найти по введеному слову/символу__.
- __"Удалить заметку": Вам даётся возможность удалить заметку, вписав в строку ввода ID заметки__.
- __"Выход": Выход из программы__.








