#!/usr/bin/env python3
import cgi
import sqlite3
import html

print("Content-type: text/html\n")

form = cgi.FieldStorage()
name = html.escape(form.getvalue('name', ''))
license = html.escape(form.getvalue('license', ''))
birth_day = html.escape(form.getvalue('birth_day', ''))
experience = form.getvalue('experience', 0)

connection = sqlite3.connect('transport.db')
cursor = connection.cursor()
cursor.execute('INSERT INTO Drivers (name, license, birth_day, experiance) VALUES (?, ?, ?, ?)',
               (name, license, birth_day, experience))
connection.commit()
connection.close()

print("<html><body>")
print("<h1>Данные добавлены!</h1>")
print("<a href='/'>Назад</a>")
print("</body></html>")
