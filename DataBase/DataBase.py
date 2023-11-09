import sqlite3

class Database:
    def __init__(self): # Инициализируем базу данных
        self.conn = sqlite3.connect("DataBase/db/notes.db") # Подключаемся к базе данных notes.db
        self.cursor = self.conn.cursor()
        self.create_table()
    
# Создание таблицы notes
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT
            )
        """)
        self.conn.commit()

# Добавление заметки в базу данных
    def add_note(self, title, content):
        self.cursor.execute("""
            INSERT INTO notes (title, content)
            VALUES (?, ?)
        """, (title, content))
        self.conn.commit()

# Получение списка заметок
    def get_all_notes(self):
        self.cursor.execute("SELECT * FROM notes")
        return self.cursor.fetchall()

# Получения заметки по ID
    def get_note_by_id(self, note_id):
        self.cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
        return self.cursor.fetchone()

# Поиск заметок по ключевому слову
    def search_notes(self, keyword):
        self.cursor.execute("SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?", ('%'+keyword+'%', '%'+keyword+'%'))
        return self.cursor.fetchall()

# Удаление заметки из базы данных
    def delete_note(self, note_id):
        self.cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.conn.commit()

# Проверка на дубликат
    def check_duplicate_note_title(self, title):
        self.cursor.execute("SELECT * FROM notes WHERE title = ?", (title,))
        return self.cursor.fetchone() is not None

