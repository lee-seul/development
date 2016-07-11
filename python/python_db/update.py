# coidng: utf-8
# select2.py

import sqlite3
from select4 import select_all_books


# 일부 조회용 함수 
def update_books():
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    update_sql = 'UPDATE my_books SET recommendation=? WHERE title=?'

    cur.execute(update_sql, (1, '개발자의 코드'))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    select_all_books()
    update_books()
    select_all_books()
