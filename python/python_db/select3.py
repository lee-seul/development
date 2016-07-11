# coidng: utf-8
# select3.py

import sqlite3

# where절 이용 조회용 함수 
def select_all_books():
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute('SELECT title, pages FROM my_books WHERE pages > 300')

    print('[3] WHERE절 이용 데이터 출력하기') 

    books = cur.fetchall()

    for book in books:
        print(book)

    conn.close()


if __name__ == '__main__':
    select_all_books()

