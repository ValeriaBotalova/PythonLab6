#!/usr/bin/env python3

import cgi
import sqlite3

print("Content-type: text/html\n")

form = cgi.FieldStorage()

id = form.getvalue('id')
name = form.getvalue('name')
license_number = form.getvalue('license')
birth_day = form.getvalue('birth_day')
experiance = form.getvalue('experiance')

try:
    connection = sqlite3.connect('transport.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE Drivers SET name = ?, license = ?, birth_day = ?, experiance = ? WHERE id = ?',
                   (name, license_number, birth_day, experiance, id))
    connection.commit()
    
    if cursor.rowcount == 0:
        print("<h3>Водитель с данным ID не найден!</h3>")
    else:
        print("<h3>Водитель изменен успешно!</h3>")
except sqlite3.Error as e:
    print(f"<h3>Ошибка базы данных: {str(e)}</h3>")
finally:
    if connection:
        connection.close()

print("<a href='/'>Назад</a>")
