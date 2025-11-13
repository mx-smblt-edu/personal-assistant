"""
Defines a custom exception for handling cases where a phone number already exists in the phone list.
"""
from colorama import Fore, Style


class AlreadyPhoneNumberError(Exception):
    """
    Custom exception to indicate that a phone number already exists in the phone list.
    """

    def __init__(self, phone: str):
        self.message = f"{Fore.RED}[ERROR]{Style.RESET_ALL} Phone '{phone}' is already used."
