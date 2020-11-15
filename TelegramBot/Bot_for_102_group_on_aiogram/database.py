import sqlite3
import os
from typing import List, Tuple, Dict

connect = sqlite3.connect("db.db")
cursor = connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users ( "
               "id_user INTEGER PRIMARY KEY,"
               "name_user VARCHAR(255), "
               "is_admin INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS homework ( "
               "id_user INTEGER,"
               "id_line INTEGER PRIMARY KEY,"
               "name_homework VARCHAR(255),"
               "data_start VARCHAR(100),"
               "deadline VARCHAR(100) ,"
               "description VARCHAR(255) )")

cursor.execute("CREATE TABLE IF NOT EXISTS links ( "
               "id_link INTEGER PRIMARY KEY,"
               "name_link VARCHAR(255),"
               "link VARCHAR(500) )")
cursor.execute("CREATE TABLE IF NOT EXISTS admins ( "
               "id_user INTEGER PRIMARY KEY )")
connect.commit()


def insert(table: str, column_values: Dict):
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ', '.join('?' * len(column_values.keys()))
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    connect.commit()


def fetchall(table: str, column: str) -> List[Tuple]:
    cursor.execute(f"SELECT {column} FROM {table}")
    return cursor.fetchall()

