import sqlite3
import math

connection = sqlite3.connect('transport.db')
cursor = connection.cursor()

cursor.execute('PRAGMA foreign_keys = ON;')

#!!!!!!!!!!!!!ТАБЛИЦА С ДАННЫМИ ВОДИТЕЛЕЙ!!!!!!!!!!!!!!
cursor.execute('''
CREATE TABLE IF NOT EXISTS Drivers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    license TEXT NOT NULL UNIQUE, 
    birth_day TEXT NOT NULL,
    experiance INTEGER
)
''')

drivers_data = [
    ('Алексей Смирнов', 'XY1234567', '1980-02-15', 15),
    ('Мария Иванова', 'EF9876543', '1995-07-22', 3),
    ('Дмитрий Кузнецов', 'GH3456789', '1987-01-10', 12),
    ('Елена Соколова', 'IJ1234567', '1992-04-08', 8),
    ('Андрей Ковалёв', 'KL9876543', '1985-11-30', 10),
    ('Ольга Фролова', 'MN1234567', '1990-05-12', 6),
    ('Сергей Васильев', 'OP9876543', '1983-09-14', 12),
    ('Анна Петрова', 'QR1234567', '1993-01-20', 5),
    ('Николай Сидоров', 'ST9876543', '1988-06-27', 8),
    ('Татьяна Михайлова', 'UV1234567', '1991-03-02', 7),
    ('Максим Орлов', 'WX9876543', '1986-12-05', 11),
    ('Ирина Лебедева', 'YZ1234567', '1994-08-18', 4),
    ('Виктор Яковлев', 'AB9876543', '1982-10-09', 11),
    ('Евгения Романова', 'CD1234567', '1989-02-04', 6),
    ('Анатолий Громов', 'EF9876543', '1984-07-15', 13),
    ('Дарья Сергеева', 'GH1234567', '1990-09-25', 5),
    ('Заславская Полина', 'IJ7654321', '1996-11-11', 2),
    ('Кирилл Архипов', 'KL5432167', '1981-01-22', 14),
    ('Наталья Дубровская', 'MN2345678', '1987-03-14', 9),
    ('Максим Смышляев', 'LM05092020', '2002-10-04', 5),
    ('Светлана Ласкова', 'QR2345678', '1992-06-30', 4)
]

insert_query = '''
INSERT OR IGNORE INTO Drivers (name, license, birth_day, experiance) VALUES (?, ?, ?, ?)
'''

cursor.executemany(insert_query, drivers_data)

#!!!!!!!!!!!!!ТАБЛИЦА С ДАННЫМИ ТРАНСПОРТА!!!!!!!!!!!!!!
cursor.execute('''
CREATE TABLE IF NOT EXISTS Transport (
    id INTEGER PRIMARY KEY,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER,
    driver_id INTEGER,
    UNIQUE (brand, model, year),
    FOREIGN KEY (driver_id) REFERENCES Drivers (id) ON DELETE SET NULL
)
''')

transport_data = [
    ('Toyota', 'Camry', 2021, 1),  
    ('Honda', 'Accord', 2019, 2),
    ('Ford', 'Mustang', 2020, 3),
    ('Chevrolet', 'Malibu', 2018, 4),
    ('BMW', '3 Series', 2022, 5),
    ('Audi', 'A4', 2021, 6),
    ('Mercedes-Benz', 'C-Class', 2020, 7),
    ('Volkswagen', 'Passat', 2019, 8),
    ('Nissan', 'Altima', 2018, 9),
    ('Suzuki', 'Swift', 2021, 10),
    ('Kia', 'Optima', 2020, 11),
    ('Hyundai', 'Sonata', 2019, 12),
    ('Subaru', 'Impreza', 2021, 13),
    ('Jeep', 'Cherokee', 2020, 14),
    ('Ram', '1500', 2022, 15),
    ('Tesla', 'Model S', 2021, 16),
    ('Lexus', 'ES', 2019, 17),
    ('Porsche', 'Cayenne', 2020, 18), 
    ('Volvo', 'S60', 2021, 19),
    ('Land Rover', 'Discovery', 2019, 20)
]

insert_query = '''
INSERT OR IGNORE INTO Transport (brand, model, year, driver_id) VALUES (?, ?, ?, ?)
'''

cursor.executemany(insert_query, transport_data)

#!!!!!!!!!!!!!ТАБЛИЦА С ДАННЫМИ ПОЕЗДОК!!!!!!!!!!!!!!!
cursor.execute('''
CREATE TABLE IF NOT EXISTS Routes (
    id INTEGER PRIMARY KEY,
    start_position TEXT NOT NULL,
    end_position TEXT NOT NULL,
    distance INTEGER,
    transport_id INTEGER,
    FOREIGN KEY (transport_id) REFERENCES Transport (id) ON DELETE CASCADE,
    UNIQUE (start_position, end_position)
)
''')

# Пример идентификаторов транспортных средств для маршрутов
routes_data = [
    ('Москва', 'Екатеринбург', 1661, 1),
    ('Новосибирск', 'Томск', 217, 2),
    ('Санкт-Петербург', 'Калуга', 347, 3),
    ('Нижний Новгород', 'Кострома', 117, 4),
    ('Владивосток', 'Хабаровск', 759, 5),
    ('Уфа', 'Саранск', 387, 6),
    ('Казань', 'Чебоксары', 240, 7),
    ('Ростов-на-Дону', 'Волгоград', 390, 8),
    ('Самара', 'Тольятти', 70, 9),
    ('Махачкала', 'Грозный', 147, 10),
    ('Сочи', 'Туапсе', 128, 11), 
    ('Астрахань', 'Волгоград', 145, 12),
    ('Ярославль', 'Кострома', 90, 13),
    ('Пенза', 'Саратов', 160, 14),
    ('Тюмень', 'Ишим', 220, 15),
    ('Челябинск', 'Златоуст', 186, 16),
    ('Рязань', 'Симферополь', 890, 17),
    ('Калуга', 'Москва', 160, 18),
    ('Смоленск', 'Вязьма', 120, 19),
    ('Биробиджан', 'Советская Гавань', 155, 20)
]

insert_query = '''
INSERT OR IGNORE INTO Routes (start_position, end_position, distance, transport_id) VALUES (?, ?, ?, ?)
'''

cursor.executemany(insert_query, routes_data)

connection.commit()

cursor.execute('SELECT COUNT(*) FROM Routes')
total_routes = cursor.fetchone()[0]
print(f"\nКоличество маршрутов: {total_routes}")

cursor.execute('SELECT AVG(experiance) FROM Drivers')
average_experience = cursor.fetchone()[0]
print(f"\nСредний стаж водителей: {round(average_experience)} лет")

cursor.execute('SELECT brand,model FROM Transport JOIN Drivers ON Transport.driver_id = Drivers.id WHERE Drivers.experiance > ?',(4,))
good_transports = cursor.fetchall()
print("\nТранспорт, управляемый опытными водителями:")
for transport in good_transports:
    print(transport)
connection.close()
