import mysql.connector
from mysql.connector import Error


                            #  СОЗДАНИЕ, УДАЛЕНИЕ, ИЗМЕНЕНИЕ И ПОДКЛЮЧЕНИЕ К БД (создание таблиц)


# по сути тут мы подключаемся к базе данных все параметры вроде как понятно
# что бы подключиться не к кокретной базе данных а просто к пространству с базами данных, мы можем не передавать
#           параметр "db_name" и потом использовать запись USE "название базы данных"
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name)
        print("Успешно подключился к БД")
    except Error as e:
        print(f"Ошибка '{e}' ")
    return connection


# Тот же пример что и выше но только без подключения к определенной базе данных, мы тут просто подключаемся к серверу
def create_connection1(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,)
        print("Успешно подключился к БД")
    except Error as e:
        print(f"Ошибка '{e}' ")

    return connection


# здесь я подключился к своей базе данных созданной ранее sm_app
connection = create_connection("localhost", "root", "root", "sm_app")



                                 # ДЕЛАЕТ ЗАПРОС В БАЗУ ДАННЫХ



def query_to_DB(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Запрос выполнен")
    except Error as e:
             print(f"Ошибка '{e}' ")



                                                        # ЗАПИСЬ В БД (таблицы)


# ПРИМЕР добавления данных в таблицу
query_to_BD = """INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);"""

query_to_DB(connection, query_to_BD)
# вызываем метод коммит для записи, иначе не записывает
connection.commit()
connection.close()



                            # ЧТЕНИЕ ИЗ БД



# эта функция умеет читать данные из базы данных просто нужно написать селект нужный и все, выведится список с данными
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# ПРИМЕР. здесь я подключился к своей БД и вывел через запрос записи в которых Id > 5
connection = create_connection("localhost", "root", "root", "makhunov")
select_users = "SELECT * FROM users WHERE id > 5"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)

