"""This module contains event handler logic"""
from typing import Union, List, Dict

from database import Database
from account import Account


class EventHandler:

    def __init__(self):
        self._db = Database()

    def get_accounts(self) -> List[Account]:
        accounts = []
        import pdb; pdb.set_trace
        select_accounts = (
            "SELECT "
            "first_name,"
            "last_name,"
            "email,"
            "gender,"
            "iban,"
            "crncy,"
            "balance "
            "FROM \"Accounts\";"
        )

        select_res = self._db.fetch(select_accounts)

        if select_res and select_res[0] is not None:
            for res in select_res:
                (f_name,
                 l_name,
                 email,
                 gender,
                 iban,
                 crncy,
                 balance,
                 ) = res
                account = Account(first_name=f_name,
                                  last_name=l_name,
                                  email=email,
                                  gender=gender,
                                  iban=iban,
                                  crncy=crncy,
                                  balance=balance,
                                  )
                accounts.append(account)

        return accounts

    def get_account(self, iban: str) -> Account:
        account = None

        select_account = (
            "SELECT "
            "first_name,"
            "last_name,"
            "email,"
            "gender,"
            "iban,"
            "crncy,"
            "balance "
            "FROM \"Accounts\" "
            "WHERE iban = %s;"
        )

        select_res = self._db.fetch(select_account, iban)

        if select_res and select_res[0] is not None:
            (f_name,
             l_name,
             email,
             gender,
             iban,
             crncy,
             balance) = select_res[0]
            account = Account(first_name=f_name,
                              last_name=l_name,
                              email=email,
                              gender=gender,
                              iban=iban,
                              crncy=crncy,
                              balance=balance,
                              )
        return account

    def upsert_account(self, form: Dict[str, Union[str, float]]) -> bool:
        upsert_accounts = (
            "INSERT INTO \"Accounts\" "
            "("
            "first_name,"
            "last_name,"
            "email,"
            "gender,"
            "iban,"
            "crncy,"
            "balance) "
            "VALUES "
            "(%s, %s, %s, %s, %s, %s, %s) "
            "ON CONFLICT (iban) DO UPDATE SET "
            "first_name = EXCLUDED.first_name,"
            "last_name = EXCLUDED.last_name,"
            "email = EXCLUDED.email,"
            "gender = EXCLUDED.gender,"
            "crncy = EXCLUDED.crncy,"
            "balance = EXCLUDED.balance;"

        )

        first_name = form.get('first_name')
        last_name = form.get('last_name')
        email = form.get('email')
        gender = form.get('gender')
        iban = form.get('iban')
        crncy = form.get('crncy')
        balance = form.get('balance')

        return self._db.execute(upsert_accounts, first_name, last_name,
                                email, gender, iban, crncy, balance)

    def delete_account(self, form: Dict[str, Union[str, float]]) -> bool:
        delete_accounts = (
            "DELETE FROM \"Accounts\" "
            "WHERE iban = %s;"
        )

        iban = form.get('iban')

        return self._db.execute(delete_accounts, iban)
