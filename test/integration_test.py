"""This module contains integration tests for this application"""
import unittest
from unittest.mock import patch
import os

from dotenv import load_dotenv

from src.event_handler import EventHandler
from src.account import Account
from test.test_database import TestDatabase

load_dotenv('.env.test')


class EventHandlerShouldReadAccounts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_db = TestDatabase()
        cls.event_handler = EventHandler()

    def test_retrieves_account(self):
        account = self.event_handler.get_account('BH56 ZQPE KMTY NLIM ZYQ8 7K')

        self.assertEqual(account.balance, 29.54)
        self.assertEqual(account.crncy, 'EUR')
        self.assertEqual(account.email, 'tberceros2@hc360.com')
        self.assertEqual(account.first_name, 'Trudi')
        self.assertEqual(account.gender, 'Genderfluid')
        self.assertEqual(account.iban, 'BH56 ZQPE KMTY NLIM ZYQ8 7K')
        self.assertEqual(account.last_name, "Berceros")

    def test_retrieves_accounts(self):
        accounts = self.event_handler.get_accounts()
        self.assertGreater(len(accounts), 1)

    def test_inserts_accounts(self):
        test_dict = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'gender': 'Gender',
            'iban': 'IBAN',
            'crncy': 'Currency',
            'balance': 12345
        }

        accounts = self.event_handler.upsert_account(test_dict)

        select = (
            "SELECT email FROM \"Accounts\" WHERE iban = %s;"
        )

        res = self.test_db.fetch(select, 'IBAN')

        self.assertEqual(res[0][0], 'Email')

    def test_upserts_accounts(self):
        test_dict = {
            'first_name': 'Upsert First Name',
            'last_name': 'Upsert Last Name',
            'email': 'Upsert Email',
            'gender': 'Upsert Gender',
            'iban': 'PL38 0462 5893 3715 8610 7657 0112',
            'crncy': 'Upsert Currency',
            'balance': 12345
        }

        accounts = self.event_handler.upsert_account(test_dict)

        select = (
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

        (
            first_name,
            last_name,
            email,
            gender,
            iban,
            crncy,
            balance
        ) = self.test_db.fetch(
            select, 'PL38 0462 5893 3715 8610 7657 0112')[0]

        self.assertEqual(balance, 12345.0)
        self.assertEqual(crncy, 'Upsert Currency')
        self.assertEqual(email, 'Upsert Email')
        self.assertEqual(first_name, 'Upsert First Name')
        self.assertEqual(gender, 'Upsert Gender')
        self.assertEqual(iban, 'PL38 0462 5893 3715 8610 7657 0112')
        self.assertEqual(last_name, 'Upsert Last Name')

    def test_upserts_accounts(self):
        test_dict = {
            'first_name': 'Upsert First Name',
            'last_name': 'Upsert Last Name',
            'email': 'Upsert Email',
            'gender': 'Upsert Gender',
            'iban': 'PL38 0462 5893 3715 8610 7657 0112',
            'crncy': 'Upsert Currency',
            'balance': 12345
        }

        accounts = self.event_handler.upsert_account(test_dict)

        select = (
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

        (
            first_name,
            last_name,
            email,
            gender,
            iban,
            crncy,
            balance
        ) = self.test_db.fetch(
            select, 'PL38 0462 5893 3715 8610 7657 0112')[0]

        self.assertEqual(balance, 12345.0)
        self.assertEqual(crncy, 'Upsert Currency')
        self.assertEqual(email, 'Upsert Email')
        self.assertEqual(first_name, 'Upsert First Name')
        self.assertEqual(gender, 'Upsert Gender')
        self.assertEqual(iban, 'PL38 0462 5893 3715 8610 7657 0112')
        self.assertEqual(last_name, 'Upsert Last Name')

    def test_deletes_accounts(self):
        test_dict = {
            'first_name': 'TO_BE_DELETED First Name',
            'last_name': 'TO_BE_DELETED Last Name',
            'email': 'TO_BE_DELETED Email',
            'gender': 'TO_BE_DELETED Gender',
            'iban': 'TO_BE_DELETED IBAN',
            'crncy': 'TO_BE_DELETED Currency',
            'balance': -1
        }

        accounts = self.event_handler.upsert_account(test_dict)

        select = (
            "SELECT iban "
            "FROM \"Accounts\" "
            "WHERE iban = %s;"
        )

        (iban) = self.test_db.fetch(
            select, 'TO_BE_DELETED IBAN')[0][0]

        self.assertEqual(iban, 'TO_BE_DELETED IBAN')

        iban_deletion = {
            'iban': 'TO_BE_DELETED IBAN'
        }

        self.event_handler.delete_account(iban_deletion)

        select = (
            "SELECT iban "
            "FROM \"Accounts\" "
            "WHERE iban = %s;"
        )

        acc_res = self.test_db.fetch(
            select, 'TO_BE_DELETED IBAN')
        self.assertSequenceEqual(acc_res, [])


if __name__ == "__main__":
    unittest.main()
