#!/usr/bin/env python3

import psycopg2
import sys

try:
    conn = psycopg2.connect(dbname='bench_db', user='postgres', host='localhost')
except psycopg2.Error as e:
    print(e)
    sys.exit(1)

cur = conn.cursor()

cur.execute("SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'results_result'")
conn.commit()

rows = cur.fetchall()

for row in rows:
    print(row[0])

cur.close()
conn.close()


