#с помощью листа добавлять номера
import psycopg2
from config import config

file = open('csv.txt', 'r')
a = file.read().split()
file.close()


def insert_user_list(user_list):
    sql = """

    insert into phonebook(username,phone) values (%s, %s)

    """

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql, user_list)
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()


cnt = 0
while cnt < len(a):
    insert_user_list([
        (a[cnt], a[cnt + 1])
    ])
    cnt += 2