"""
Provides an AddressBook class for managing and storing contact information.
"""
from collections import UserDict
from src.model.contact import Contact
from src.model.name import Name


class ContactBook(UserDict[Name, Contact]):
    """A class for storing and managing contacts."""

    def __str__(self) -> str:
        return "ContactBook\n" + '\n'.join([f'{record}' for record in self.data.values()])
