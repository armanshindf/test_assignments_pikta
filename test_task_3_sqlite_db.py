"""
Implements a sqlite3 database creation with terminal output
"""

import sqlite3

with sqlite3.connect("task3.db") as conn:
    cursor = conn.cursor()


def db_output(cursor):
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def create_db():
    cursor.execute('''
            CREATE TABLE products(product_id integer PRIMARY KEY,
            product_name text, price real);
            ''')

    cursor.execute('''
            CREATE TABLE clients(client_id integer PRIMARY KEY,
            client_name text);
            ''')

    cursor.execute('''
            CREATE TABLE orders(order_id integer PRIMARY KEY,
            client_id integer, product_id integer, order_name text,
            FOREIGN KEY (client_id) references clients(client_id),
            FOREIGN KEY (product_id) references products(product_id));
            ''')

    client = [(1, 'Иван'),
              (2, 'Констанин'),
              (3, 'Дмитрий'),
              (4, 'Александр')]

    product = [(1, 'Мяч', 299.99),
               (2, 'Ручка', 18),
               (3, 'Кружка', 159.87),
               (4, 'Монитор', 18000),
               (5, 'Телефон', 9999.9),
               (6, 'Кофе', 159)]

    order = [(1, 2, 2, 'Закупка 1'),
             (2, 2, 5, 'Закупка 2'),
             (3, 2, 1, 'Закупка 3'),
             (4, 1, 1, 'Закупка 4'),
             (5, 1, 3, 'Закупка 5'),
             (6, 1, 6, 'Закупка 6'),
             (7, 1, 2, 'Закупка 7'),
             (8, 4, 5, 'Закупка 8'),
             (9, 3, 6, 'Закупка 9'),
             (10, 3, 3, 'Закупка 10'),
             (11, 1, 5, 'Закупка 11')]
    cursor.executemany("INSERT INTO clients VALUES (?,?)", client)

    cursor.executemany("INSERT INTO products VALUES (?,?,?)", product)

    cursor.executemany("INSERT INTO orders VALUES (?,?,?,?)", order)

    print('Таблицы успешно созданы')
    print('Таблица clients:')
    cursor.execute("select * from clients")
    db_output(cursor)

    print('Таблица products:')
    cursor.execute("select * from products")
    db_output(cursor)

    print('Таблица orders:')
    cursor.execute("select * from orders")
    db_output(cursor)


def clients_summ():
    query = ('''
                SELECT client_name, sum(price)
                from clients
                join orders on orders.client_id = clients.client_id
                join products on products.product_id = orders.product_id
                group by client_name
                ''')
    cursor.execute(query)
    print('Cписок клиентов с общей суммой их покупки:')
    print(cursor.fetchall())


def clients_phone():
    query = (
        '''
        SELECT client_name
        from clients
        join orders on orders.client_id = clients.client_id
        join products on products.product_id = orders.product_id
        where products.product_id = 5
        '''
    )
    cursor.execute(query)
    print('Клиенты, купившие телефон: ')
    print(cursor.fetchall())


def products_orders():
    query = (
        '''
        SELECT product_name, count(orders.product_id)
        from products
        join orders on orders.product_id = products.product_id
        group by product_name
        '''
    )
    cursor.execute(query)
    print('Всего продано: ')
    print(cursor.fetchall())

create_db()
clients_summ()
clients_phone()
products_orders()

