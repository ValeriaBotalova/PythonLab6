#!/usr/bin/env python3
import sqlite3

print("Content-type: text/html\n")
print("<html><body>")
print("<h1>Список водителей</h1>")

connection = sqlite3.connect('transport.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM Drivers')
drivers = cursor.fetchall()

print("<table border='1'>")
print("<tr><th>ID</th><th>Имя</th><th>Лицензия</th><th>Дата Рождения</th><th>Стаж</th></tr>")
for driver in drivers:
    print(f"<tr><td>{driver[0]}</td><td>{driver[1]}</td><td>{driver[2]}</td><td>{driver[3]}</td><td>{driver[4]}</td></tr>")
print("</table>")

connection.close()
print("<a href='/'>Назад</a>")
print("</body></html>")

