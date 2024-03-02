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
    BOOOL = ("FALSE","TRUE")
    for i in range(3000000):
        query="""INSERT INTO contracts(number, date_begin, price, description, client, real_estate_agency, apartment) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        item_tuple=(fake.ssn(),
                    fake.date(),
                    random.randint(1000,990000),
                    "description",
                    random.randint(1, 300000),
                    random.randint(3, 100000),
                    random.randint(9, 300000),
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