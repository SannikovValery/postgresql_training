import psycopg2
from config import host, user, password, db_name

try:
    # connecting to existing database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name)
    connection.autocommit = True  # commiting changes to database,can be manually set for every action of auto= True
    # create a cursor object to navigate and work with database.
    with connection.cursor() as cursor:
        cursor.execute('SELECT VERSION()')  # execution of SQL commands

        print(f"Server version: {cursor.fetchone()}")  # fetch returns a tuple or None if no data available
    # # creating new table
    # with connection.cursor() as cursor:
    #     cursor.execute("""CREATE TABLE users(
    #     id serial PRIMARY KEY,
    #     first_name varchar(50) NOT NULL,
    #     nick_name varchar(50) NOT NULL );""")
    #
    #     print('[INFO]Table successfully created!')
    # creating specific columns with values
    # with connection.cursor() as cursor:
    #     cursor.execute("""
    #     INSERT INTO users(first_name,nick_name)VALUES
    #                    ('Valery','Oldest_junior');""")
    #     print('[INFO]Data was successfully inserted!')
    # get a data from table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT nick_name FROM users WHERE first_name='Valery';""")
    #     print(cursor.fetchone())

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users;""")
    #     print("Table was deleted")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection closed')
