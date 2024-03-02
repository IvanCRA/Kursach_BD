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
    TYPE_TR = ("DIRECTOR","SAME_WORK","OFFICEMAN","NOOB","PROGRAMMIST","RENTMAN")
    for i in range(300000):
        query="""INSERT INTO workers(full_name, type_work, passport, phone_number, real_estate_agence) VALUES (%s,%s,%s,%s,%s)"""
        item_tuple=(fake.name(),
                    TYPE_TR[random.randint(1, len(TYPE_TR) - 1)],
                    fake.ssn(),
                    fake.phone_number(),
                    random.randint(3,100000)
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