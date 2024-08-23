import sqlite3

connection = sqlite3.connect('not_telegram.db ')
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

# cursor.execute('Update Users SET balance = 500 WHERE id % 2 = 1')


users = cursor.execute('SELECT * FROM Users WHERE age != ?', (60,)).fetchall()

for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')


connection.commit()
connection.close()
