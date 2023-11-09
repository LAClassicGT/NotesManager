import colorama
from DataBase.DataBase import Database

colorama.init() # Инициализируем цвета

# Определяем класс NotesManager
class NotesManager:
    def __init__(self):
        self.db = Database() # Инициализируем базу данных ( Database.py)

# Функция добавления заметок
    def add_note(self, title, content):
        if self.db.check_duplicate_note_title(title): # Проверка на дубликат
            print("")
        else:
            self.db.add_note(title, content) # Добавляем заметку в базу данных

# Функция просмотра списка заметок
    def view_notes(self):
        notes = self.db.get_all_notes() # Получаем список заметок
        for note in notes:
            print(colorama.Fore.LIGHTYELLOW_EX + f"\nID заметки: {note[0]}" + colorama.Fore.LIGHTCYAN_EX + f"\nНазвание заметки: {note[1]}\n") # Выводим "ID заметки: {id} | Название заметки: {title}"

# Функция просмотра содержимого заметки
    def view_note_content(self, note_id):
        note = self.db.get_note_by_id(note_id) # Получаем заметку по ID
        if note:
            print(colorama.Fore.LIGHTYELLOW_EX + f"\nСодержание заметки (ID: {note[0]}):" + colorama.Fore.LIGHTGREEN_EX)
            print(note[2])
            print("") # Содержание заметки (ID: {id}) | {content}"

# Функция поиска заметок по ключевому слову
    def search_notes(self, keyword):
        notes = self.db.search_notes(keyword) # Находим заметку по ключевому слову
        for note in notes:
            print(colorama.Fore.LIGHTYELLOW_EX + f"\nID заметки: {note[0]}" + colorama.Fore.LIGHTCYAN_EX + f"\nНазвание заметки: {note[1]}\n") # Выводим "ID заметки: {id} | Название заметки: {title}"

# Функция удаления заметки
    def delete_note(self, note_id):
        self.db.delete_note(note_id) # Удаляем заметку из базы данных

    colorama.deinit()
