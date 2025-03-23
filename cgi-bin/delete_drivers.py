#!/usr/bin/env python3

import cgi
import sqlite3

print("Content-type: text/html\n")
form = cgi.FieldStorage()

driver_id = form.getvalue("id")
connection = sqlite3.connect('transport.db')
cursor = connection.cursor()

cursor.execute('DELETE FROM Drivers WHERE id = ?', (driver_id,))
connection.commit()    
print("<h3>Водитель удален успешно!</h3>")
print("<a href='/'>Назад</a>")
connection.close()