import random

class UserAccount:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.username = self.get_username()
        self.password = self.get_password()

    def get_username(self):
        """Generate a username from first and last name."""
        first_initial = self.first_name[0].lower()
        last_part = self.last_name[-3:].lower() if len(self.last_name) >= 3 else self.last_name.lower()
        return first_initial + last_part

    def get_random_letter(self):
        """Return a random letter (50% chance uppercase)."""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        letter = random.choice(alphabet)
        if random.randint(0, 1):
            return letter.upper()
        return letter

    def get_random_symbol(self):
        """Return a random symbol."""
        symbols = "/*?£$()@<>^"
        return random.choice(symbols)

    def check_char(self, pw, i, char):
        """Ensure the new character is not the same as the previous one."""
        if i == 0 or char != pw[i - 1]:
            pw += char
            return True, pw
        return False, pw

    def get_password(self, length=10):
        """Generate a random password following the rules."""
        pw = ""
        for i in range(length):
            likelihood = random.randint(1, 3)
            if likelihood in (2, 3):
                # letters (more likely)
                while True:
                    char = self.get_random_letter()
                    ok, pw = self.check_char(pw, i, char)
                    if ok:
                        break
            else:
                # symbol or number
                if random.randint(1, 2) == 1:
                    # symbol
                    while True:
                        char = self.get_random_symbol()
                        ok, pw = self.check_char(pw, i, char)
                        if ok:
                            break
                else:
                    # number
                    while True:
                        char = str(random.randint(0, 9))
                        ok, pw = self.check_char(pw, i, char)
                        if ok:
                            break
        return pw

