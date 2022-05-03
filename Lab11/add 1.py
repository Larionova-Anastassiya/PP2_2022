import psycopg2
from config import config


def insert_account(username, phone):
    sql = """
    INSERT INTO accounts(username, phone)
    VALUES(%s, %s) RETURNING user_id;
    """

    conn = None
    user_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username, phone))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

    return user_id

insert_account('Almas', '83456789431')
# insert_account("Dina", '87654324321')
insert_account('Nastya', '87056662430')

nam = input()
pho = input()
insert_account(nam, pho)


"""
чтобы вывести все данные из таблицы надо ввести в консоль 
select * from insert_account 

чтобы вывести определенные данные из таблицы надо ввести в консоль 
select number from account where phone = 8707

"""