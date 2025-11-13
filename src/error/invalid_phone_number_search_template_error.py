"""
Exception raised for invalid phone number search templates.

This exception is used to indicate that the provided phone number search
template does not meet the expected format or requirements.
"""
from colorama import Fore, Style


class InvalidPhoneNumberSearchTemplateError(Exception):
    """
    Represents an error raised for an invalid phone number search template.

    This exception is specifically used to indicate that the provided phone number
    search template is not valid. It can be used in contexts where user-defined
    templates for searching phone numbers must adhere to a certain format.
    """

    def __init__(self, template: str):
        self.message = f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid phone number search template: '{template}'."

    def __str__(self) -> str:
        return self.message
