import pytest

from inventory.account import UserAccount

# --- FIXTURE SECTION ---
@pytest.fixture
def sample_user():
    """Fixture that returns a UserAccount instance."""
    return UserAccount("Alice", "Johnson")


# --- TESTS SECTION ---
def test_username_standard_case(sample_user):
    assert sample_user.username == "ason"  # first initial + last 3 letters


def test_username_short_last_name():
    user = UserAccount("John", "Li")
    assert user.username == "jli"  # handles short last names


def test_password_length(sample_user):
    assert len(sample_user.password) == 10


def test_password_no_double_characters(sample_user):
    pw = sample_user.password
    assert all(pw[i] != pw[i + 1] for i in range(len(pw) - 1))


def test_password_contains_valid_chars(sample_user):
    pw = sample_user.password
    valid_symbols = set("/*?£$()@<>^")
    valid_letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    valid_digits = set("0123456789")

    for c in pw:
        assert c in valid_letters or c in valid_digits or c in valid_symbols


def test_multiple_passwords_are_different():
    user1 = UserAccount("Alice", "Smith")
    user2 = UserAccount("Alice", "Smith")
    assert user1.password != user2.password