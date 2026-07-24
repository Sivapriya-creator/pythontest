import os
import sqlite3

# BUG: hardcoded secret (security issue)
API_KEY = "sk-live-1234567890abcdef"
PASSWORD = "admin123"


def divide(a, b):
    # BUG: no check for division by zero
    return a / b


def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SECURITY BUG: SQL injection via string formatting
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cursor.execute(query)
    return cursor.fetchall()
    # BUG: connection never closed


def read_file(path):
    # BUG: file handle never closed, no error handling
    f = open(path)
    data = f.read()
    return data


def run_command(cmd):
    # SECURITY BUG: command injection
    os.system("echo " + cmd)


def calculate_total(items):
    total = 0
    # BUG: off-by-one, skips last item
    for i in range(len(items) - 1):
        total += items[i]
    return total


def find_max(numbers):
    # BUG: crashes on empty list, wrong initial value
    max_val = 0
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val


# BUG: mutable default argument
def append_item(item, target=[]):
    target.append(item)
    return target


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        # BUG: no check for insufficient funds or negative amount
        self.balance -= amount
        return self.balance


# STYLE: unused import, unused variable, no main guard
unused_variable = 42
result = divide(10, 0)
print(get_user("1 OR 1=1"))
