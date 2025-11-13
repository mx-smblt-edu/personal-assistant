"""
Defines a custom exception class for handling unknown phone numbers.
"""
from colorama import Fore, Style


class UnknownPhoneNumberError(Exception):
    """
    Exception raised for referencing an unknown phone number.
    """

    def __init__(self, phone: str):
        self.message = f"{Fore.RED}[ERROR]{Style.RESET_ALL} Phone '{phone}' is unknown."
