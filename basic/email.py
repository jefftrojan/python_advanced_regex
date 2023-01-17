import re

def checker(email):
    email = ""
    email_pattern = '\b[A-Za-z0-9._%+-]+@[A_Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    check = re.match(email, email_pattern)

    if check:
        print("Email is valid")
    else:
        print("Invalid email format")

if __name__ == '__main__':
    email = "test@jeff.trojan"
    checker(email)