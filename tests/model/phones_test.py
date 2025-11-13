"""
Unit tests for validating the behavior of adding and removing phone numbers
in the `Phones` collection.
"""
import pytest

from src.error.already_phone_number_error import AlreadyPhoneNumberError
from src.error.unknown_phone_number_error import UnknownPhoneNumberError
from src.model.phone import Phone
from src.model.phones import Phones


def test_add_non_existing_phone() -> None:
    """
    Tests adding unique phone number to Phones.
    """
    phones = Phones()
    phone = Phone("1234567890")

    result = phones.add(phone)

    assert result == phone
    assert len(phones) == 1
    assert phone in phones.data


def test_add_duplicate_phone_returns_none() -> None:
    """
    Tests that adding a duplicate phone number returns None.
    """
    phones = Phones()
    phone = Phone("1234567890")

    phones.add(phone)
    result = phones.add(phone)

    assert result is None
    assert len(phones) == 1


def test_add_multiple_unique_phone_numbers():
    """
    Test that multiple unique phone numbers can be added to list phones.
    """
    phones = Phones()
    phone1 = Phone("1234567890")
    phone2 = Phone("0987654321")

    result1 = phones.add(phone1)
    result2 = phones.add(phone2)

    assert result1 == phone1
    assert result2 == phone2
    assert len(phones.data) == 2
    assert phones.data == [phone1, phone2]


def test_remove_phone_successful():
    """
    Test that remove_phone successfully removes an existing phone from the contact.
    """
    phones = Phones()
    phone = Phone("1234567890")
    phones.add(phone)

    removed_phone = phones.remove(phone)

    assert removed_phone == phone
    assert len(phones.data) == 0


def test_remove_nonexistent_phone():
    """
    Test that remove_phone returns None when trying to remove a phone that does not exist.
    """
    phones = Phones()
    phone1 = Phone("1234567890")
    phone2 = Phone("0987654321")

    phones.add(phone1)
    removed_phone = phones.remove(phone2)

    assert removed_phone is None


def test_remove_phone_from_empty_list():
    """
    Test that remove_phone returns None when the contact has no phone numbers.
    """
    phones = Phones()
    phone = Phone("1234567890")

    removed_phone = phones.remove(phone)

    assert removed_phone is None


def test_change_phone_successful():
    """
    Test if `replace` successfully replaces an old phone number with a new one.
    """
    phones = Phones()
    old_phone = Phone("1234567890")
    new_phone = Phone("0987654321")

    phones.add(old_phone)
    replaced_phone = phones.replace(old_phone, new_phone)

    assert replaced_phone == new_phone
    assert new_phone in phones.data
    assert old_phone not in phones.data


def test_change_phone_old_number_not_found():
    """
    Test if `replace` raises error when the old phone number doesn't exist.
    """
    phones = Phones()
    old_phone = Phone("1234567890")
    new_phone = Phone("0987654321")

    with pytest.raises(UnknownPhoneNumberError):
        phones.replace(old_phone, new_phone)


def test_change_phone_new_number_already_exists():
    """
    Test if `replace` raises error when the new phone number is already in the list.
    """
    phones = Phones()
    old_phone = Phone("1234567890")
    another_phone = Phone("1122334455")
    new_phone = Phone("1122334455")

    phones.add(old_phone)
    phones.add(another_phone)

    with pytest.raises(AlreadyPhoneNumberError):
        phones.replace(old_phone, new_phone)
