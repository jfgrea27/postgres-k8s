"""This module contains database logic"""
import os 

import sqlite3


class Database:
    def __init__(self) -> None:
        self.db_name = os.environ.get('DB_NAME')

    def execute(self, sql: str, data):
        return self._execute(sql, False, data)

    def execute_many(self, sql: str, data):
        return self._execute(sql, True, data)
    
    def _execute(self, sql: str, execute_many: bool, data):
        try:
            con = sqlite3.connect(self.db_name)

            cur = con.cursor()
            
            if execute_many:
                data = cur.executemany(sql, data).fetchall()
            else:
                data = cur.execute(sql, data).fetchall()
            
            con.commit()
            return data
        except Exception as e:  # TODO define Exception
            print(e)


# TODO remove this



with open('data/data.csv') as file:
    data = file.readlines()

    formated_data = []
    for line in data:
        field_separated = line.split(',')
        formated_data.append(field_separated)

    db = Database()

    insert_sql = (
        "INSERT INTO main.Accounts( "
	        "id,"
	        "first_name,"
	        "last_name,"
	        "email,"
	        "gender,"
	        "account_number,"
	        "crncy,"
	        "balance) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?);")
    db.execute_many(insert_sql, formated_data)
