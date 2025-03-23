#!/usr/bin/env python3

import cgi
import sqlite3

print("Content-type: text/html\n")

form = cgi.FieldStorage()

name = form.getvalue('name')
license_number = form.getvalue('license')
birth_day = form.getvalue('birth_day')
experiance = form.getvalue('experiance')

connection = sqlite3.connect('transport.db')
cursor = connection.cursor()
        
cursor.execute('INSERT INTO Drivers (name, license, birth_day, experiance) VALUES (?, ?, ?, ?)',
                       (name, license_number, birth_day, experiance))
connection.commit()    
print("<h3>Водитель добавлен успешно!</h3>")
print("<a href='/'>Назад</a>")
connection.close()
