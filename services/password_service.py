import random
import string

class PasswordService:

    def generate(self, length):
        chars = string.ascii_letters + string.digits
        password = ""

        for i in range(length):
            password += random.choice(chars)

        return password
