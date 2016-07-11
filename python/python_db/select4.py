# coidng: utf-8
# select4.py

import sqlite3

# 1개 데이터 조회용 함수 
def select_all_books():
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM my_books')

    print('[4] 일부 데이터 출력하기') 

    print(cur.fetchone())

    conn.close()


if __name__ == '__main__':
    select_all_books()
