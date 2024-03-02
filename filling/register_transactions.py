import sys
import random
from faker import Faker
from faker.providers import internet
from datetime import datetime,date ,time
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from datetime import timedelta, datetime
import psycopg2
from psycopg2 import Error
fake=Faker()
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="van0")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Выполнение SQL-запроса
    TYPE_TR = ("buy","sell","rent")
    for i in range(150000):
        query="""INSERT INTO register_transactions(title, real_estate_agence, type_transaction) VALUES (%s,%s,%s)"""
        item_tuple=(TYPE_TR[random.randint(0, len(TYPE_TR) - 1)],
                    random.randint(3,100000),
                    random.randint(1,50000),
                    )
        cursor.execute(query,item_tuple)          
    connection.commit()
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")