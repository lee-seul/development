# coding:utf-8
# test_sqlite3_1.py

import sqlite3

query = """
CREATE TABLE test(
		a VARCHAR(20), b VARCHAR(20),
		c REAL, d INTEGER
		);
"""

con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()


data = [('Atlanta', 'Georgia', 12.5, 6),
	 ('Tallahassee', 'Florida', 2.6, 3),
	 ('Sacramento', 'California', 1.7, 5)]
	
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data,)
con.commit()
