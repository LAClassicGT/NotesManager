import os
import time
import sys
import colorama
from NotesManager.NotesManager import NotesManager

def main():
    manager = NotesManager() # Инициализируем модуль
    colorama.init() # Инициализируем цвета
    
    while True:
    # Создаем меню
        print(colorama.Fore.LIGHTRED_EX + "\nМенеджер заметок" + colorama.Fore.WHITE + "." + colorama.Fore.LIGHTCYAN_EX + "Меню\n")
        print(colorama.Fore.WHITE + "1." + colorama.Fore.LIGHTCYAN_EX + "Добавить заметку.")
        print(colorama.Fore.WHITE + "2." + colorama.Fore.LIGHTRED_EX + "Просмотреть список заметок.")
        print(colorama.Fore.WHITE + "3." + colorama.Fore.LIGHTCYAN_EX + "Поиск заметки по ключевому слову.")
        print(colorama.Fore.WHITE + "4." + colorama.Fore.LIGHTRED_EX + "Удалить заметку.")
        print(colorama.Fore.WHITE + "5." + colorama.Fore.LIGHTCYAN_EX + "Выйти.")

        choice = input(colorama.Fore.LIGHTCYAN_EX + "Выберите действие: ")

    # Идентифицируем действие "Добавить заметку"
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear') # Чистим терминал от прошлого вывода
            title = input(colorama.Fore.LIGHTRED_EX + "Введите название заметки: ")
            content = input(colorama.Fore.LIGHTCYAN_EX + "Введите содержание заметки: ")
            
            print(colorama.Fore.LIGHTRED_EX + "1. Создать заметку")
            print(colorama.Fore.LIGHTCYAN_EX + "2. Отменить")         
            action = input(colorama.Fore.LIGHTCYAN_EX + "Выберите действие: ")

            if action == "1":
                manager.add_note(title, content) # Определяем функцию "Создания заметки" [NotesManager.py]
                print(colorama.Fore.LIGHTGREEN_EX + "\nЗаметка создана!\n")
            elif action == "2":
                print(colorama.Fore.LIGHTRED_EX + "Действие отменено.")

    # Идентифицируем действие "Посмотреть список заметок"
        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear') # Чистим терминал от прошлого вывода
            print(colorama.Fore.LIGHTCYAN_EX + "Список заметок:")
            manager.view_notes() # Определяем функцию "Просмотра списка заметок" [NotesManager.py]
            note_id = input(colorama.Fore.LIGHTRED_EX + "Введите ID заметки для просмотра содержания: ")
            manager.view_note_content(note_id) # Определяем функцию "Просмотра содержимого заметок" [NotesManager.py]
 
    # Идентифицируем действие "Поиск заметки по ключевому слову"
        elif choice == "3":
            os.system('cls' if os.name == 'nt' else 'clear') # Чистим терминал от прошлого вывода
            keyword = input(colorama.Fore.LIGHTCYAN_EX + "Введите ключевое слово для поиска заметки: ")
            manager.search_notes(keyword) # Определяем функцию "Поиск заметки по ключевому слову" [NotesManager.py]

    # Идентифицируем действие "Удалить заметку"
        elif choice == "4":
            os.system('cls' if os.name == 'nt' else 'clear') # Чистим терминал от прошлого вывода
            note_id = input(colorama.Fore.LIGHTRED_EX + "Введите ID заметки для удаления: ")
            manager.delete_note(note_id) # И тут тоже, мы определяем функцию, только "Удаления заметки" [NotesManager.py]
            print(colorama.Fore.LIGHTGREEN_EX + "Заметка удалена.")

    # Идентифицируем действие "Выйти"
        elif choice == "5":
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + "Неправильный выбор.. Попробуйте снова.")

    colorama.deinit()

if __name__ == "__main__":
    # Запускаем прогресс-бар в самом начале
    toolbar_width = 35 # Длина [-----------------------------------]
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))
    
    for i in range(toolbar_width):
        time.sleep(0.02) # Время прогресс-бара в секундах
        sys.stdout.write("-")
        sys.stdout.flush()
    
    sys.stdout.write("\n")
    main()
