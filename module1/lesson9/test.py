from pprint import pprint

import psycopg2
from psycopg2.extras import RealDictCursor

connect = psycopg2.connect(
    host="localhost",
    user='postgres',
    password='postgres',
    database='lesson09',
    port='5432'
)


def show_data():
    sql = "SELECT * FROM cars"
    cursor.execute(sql)
    data = cursor.fetchall()
    pprint(data)
    for item in data:
        print(item['title'])


with connect:
    cursor = connect.cursor(cursor_factory=RealDictCursor)
    show_data()