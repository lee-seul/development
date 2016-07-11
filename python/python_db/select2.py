# coidng: utf-8
# select2.py

import sqlite3

# 일부 조회용 함수 
def select_all_books(num):
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM my_books')

    print('[2] 일부 데이터 출력하기') 

    books = cur.fetchmany(num)

    for book in books:
        print(book)

    conn.close()


if __name__ == '__main__':
    select_all_books(3)
