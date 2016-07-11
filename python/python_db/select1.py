# coidng: utf-8
# select1.py

import sqlite3

# 전체 조회용 함수 
def select_all_books():
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM my_books')

    print('[1] 전체 데이터 출력하기') 

    books = cur.fetchall()

    for book in books:
        print(book)

    conn.close()


if __name__ == '__main__':
    select_all_books()
