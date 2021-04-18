"""This module contains account logic"""
from dataclasses import dataclass


@dataclass
class Account:
    first_name: str
    last_name: str
    email: str
    gender: str
    iban: str
    crncy: str
    balance: float

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "gender": self.gender,
            "iban": self.iban,
            "crncy": self.crncy,
            "balance": self.balance
        }
