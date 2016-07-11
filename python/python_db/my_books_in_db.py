# coding: utf-8
# my_books_in_db.py

import sqlite3

# 테이블 생성용 함수
def create_table():
    # 데이터베이스 커넥션 생성
    conn = sqlite3.connect('my_books.db')
    
    # 커서 확보
    cur = conn.cursor()

    # my_books 테이블 생성
    cur.execute('''CREATE TABLE my_books(title text, published_date text, publisher text,
                pages integer, recommendation integer)'''
                )
    
    # 데이터베이스 반영 
    conn.commit()

    # 커넥션 닫기 
    conn.close()

if __name__ == '__main__':
    create_table()
