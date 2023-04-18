from random import choice

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
chars = ''


count_of_passwords = int(input("Enter the number of passwords to generate: "))
password_length = int(input("Enter the length of a single password: "))
numbers = input("Should the numbers be included? (+/-): ")
upper_case = input("Should uppercase letters be included? (+/-): ")
lower_case = input("Should lowercase letters be included? (+/-): ")
characters = input("Should the characters [!#$%&*+-=?@^_] be included? (+/-): ")
ambiguous = input("Should the ambiguous characters [il1Lo0O] be excluded? (+/-): ")

if numbers == '+':
    chars += DIGITS
if upper_case == '+':
    chars += UPPERCASE_LETTERS
if lower_case == '+':
    chars += LOWERCASE_LETTERS
if characters == '+':
    chars += PUNCTUATION
if ambiguous == '+':
    for c in chars:
        chars.replace(c, '')


def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += choice(chars)
    return password


for i in range(count_of_passwords):
    print(generate_password(password_length, chars))
