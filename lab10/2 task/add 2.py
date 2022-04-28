import psycopg2
from config import config


def insert_account(username, score):
    sql = """
    INSERT INTO accounts(username, score)
    VALUES(%s, %s) RETURNING user_id;
    """

    conn = None
    user_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username, score))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

    return user_id

# insert_account('Almas', '4567')
# insert_account("Dina", '13')
insert_account('Nastya', '432')

nam = input()
pho = input()
insert_account(nam, pho)