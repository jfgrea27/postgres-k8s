"""This module contains test database logic"""
import os

import psycopg2


class TestDatabase:
    def __init__(self) -> None:
        self.db_host = os.environ.get('DB_HOST')
        self.db_name = os.environ.get('DB_NAME')
        self.db_user = os.environ.get('DB_USER')
        self.db_password = os.environ.get('DB_PASSWORD')
        self.db_port = os.environ.get('DB_PORT')

    def fetch(self, sql: str, *data):
        return self._fetch(sql, False, *data)

    def fetch_many(self, sql: str, *data):
        return self._fetch(sql, True, *data)

    def _fetch(self, sql: str, fetch_many: bool, *data):
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
