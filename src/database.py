"""This module contains database logic"""
import os

import psycopg2


class Database:
    def __init__(self) -> None:
        self.db_host = os.environ.get('DB_HOST')
        self.db_name = os.environ.get('DB_NAME')
        self.db_user = os.environ.get('DB_USER')
        self.db_password = os.environ.get('DB_PASSWORD')
        self.db_port = os.environ.get('DB_PORT')

    def execute(self, sql: str, *data) -> bool:
        return self._execute(sql, False, *data)

    def execute_many(self, sql: str, *data) -> bool:
        return self._execute(sql, True, *data)

    def _execute(self, sql: str, execute_many: bool, *data) -> bool:
        try:
            con = psycopg2.connect(
                host=self.db_host,
                database=self.db_name,
                user=self.db_user,
                password=self.db_password,
                port=self.db_port
            )

            cur = con.cursor()

            if execute_many:
                cur.executemany(sql, *data)
            else:
                cur.execute(sql, data)
            con.commit()
            return True
        except Exception as e:
            # TODO define Exception
            print(e)
            return False

    def fetch(self, sql: str, *data):
        return self._fetch(sql, False, *data)

    def fetch_many(self, sql: str, *data):
        return self._fetch(sql, True, *data)

    def _fetch(self, sql: str, fetch_many: bool, *data):
        try:
            con = psycopg2.connect(
                host=self.db_host,
                database=self.db_name,
                user=self.db_user,
                password=self.db_password
            )

            cur = con.cursor()

            if fetch_many:
                cur.executemany(sql, *data)
                data = cur.fetchall()
            else:
                cur.execute(sql, data)
                data = cur.fetchall()
            con.commit()
            return data
        except Exception as e:
            # TODO define Exception
            print(e)
