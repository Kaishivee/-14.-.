import sqlite3

connection = sqlite3.connect('not_telegram_2.db ')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON users (email)')
# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'user{i}', f'example{i}gmail.com', i * 10, 1000))

# cursor.execute('Update Users SET balance = ? WHERE id % 2 = 1 ', (500,))
#
users = cursor.execute('SELECT * FROM Users WHERE age != ?', (60,)).fetchall()
#
# cursor.execute('DELETE FROM Users WHERE id % 3 = 1').fetchall()
#
# cursor.execute('DELETE FROM Users WHERE id = ?', (6,)).fetchall()

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# for user in users:
#     print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

print(all_balances / total_users)

connection.commit()
connection.close()
