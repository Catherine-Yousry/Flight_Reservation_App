## بيحتوى على اعداد قاعدة البيانات والاتصال

import sqlite3

def init_db():
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        flight_number TEXT NOT NULL,
        departure TEXT NOT NULL,
        destination TEXT NOT NULL,
        date TEXT NOT NULL,
        seat_number TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_reservation(name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()

def get_all_reservations():
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()
    conn.close()
    return reservations

def update_reservation(id, name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE reservations SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=? WHERE id=?",
                   (name, flight_number, departure, destination, date, seat_number, id))
    conn.commit()
    conn.close()

def delete_reservation(id):
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id=?", (id,))
    conn.commit()
    conn.close()


init_db()