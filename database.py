import sqlite3


def insert_blob(id, photo, today):
    try:
        sqlite_connection = sqlite3.connect('Photos.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS Photos
                              (id serial not null, photo text not null, data datetime not null)''')
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS Rect_Photos
                              (id serial not null, photo text not null, data datetime not null)''')
        cursor.execute(f'''INSERT INTO Photos
                                  (id, photo, data) VALUES ('{id}', '{photo}', '{today}')''')
        sqlite_connection.commit()
        print("Изображение и файл успешно вставлены в таблиу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")