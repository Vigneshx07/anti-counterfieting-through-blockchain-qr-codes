import sqlite3

class Database:
    def __init__(self, db_name='products.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pid TEXT,
                    name TEXT,
                    user TEXT,
                    address TEXT,
                    digital_signature TEXT,
                    timestamp TEXT
                )
            ''')

    def insert_product(self, pid, name, user, address, digital_signature, timestamp):
        with self.connection:
            self.connection.execute('''
                INSERT INTO products (pid, name, user, address, digital_signature, timestamp)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (pid, name, user, address, digital_signature, timestamp))

    def fetch_product_by_pid(self, pid):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM products WHERE pid=?', (pid,))
        return cursor.fetchone()

    def fetch_all_products(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM products')
        return cursor.fetchall()
