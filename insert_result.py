#!/usr/bin/env python3

import psycopg2
import sys

try:
	conn = psycopg2.connect(dbname='bench_db', user='postgres', host='localhost')
except psycopg2.Error as e:
	print(e)
	sys.exit(1)

cur = conn.cursor()


def show():
	cur.execute("SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'results_result'")
	cols = cur.fetchall()
	print(" |".join(map(str,[c[0].ljust(15) for c in cols])))

	cur.execute("SELECT * FROM results_result")
	rows = cur.fetchall()

	for row in rows:
		print("	|".join([str(r).strip().ljust(15) for r in row]))


def add():
	keys = ["user", "system", "submit_time", "jobid", "nodes", "ranks", "threads", "code", "version", "compiler", "mpi", "modules", "dataset", "result", "result_unit"]
	vals = ["mcawood", "Stampede2", "2020-06-16 14:35:18-05:00", 51232, 6, 48, 4,  "wrf", 4.5, "mpi", "impi", "", "conus2km", 53.2, "seconds"]

	key_str = ", ".join(keys)
	val_str = ", ".join(["'" + str(v) + "'" for v in vals])

	print(key_str)
	print(val_str)

	try:
		print("INSERT INTO results_result (" + key_str + ") VALUES (" + val_str + ");")
		cur.execute("INSERT INTO results_result (" + key_str + ") VALUES (" + val_str + ");")
		conn.commit()
	except psycopg2.Error as e:
		print(e)


#show()
add()

cur.close()
conn.close()

