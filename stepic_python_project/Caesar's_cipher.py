eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

action = input("Enter the action: encrypt(e) or decrypt(d):\n")
while action != 'e' and action != 'd':
    action = input("Something went wrong! You can enter only 'e' or 'd'\n")

lang = input("Enter the language: English(en) or Russian(ru):\n")
while lang != 'en' and lang != 'ru':
    lang = input("Something went wrong! You can enter only 'en' or 'ru'\n")

steps = input("Enter shift step(number):\n")
while not steps.isdigit():
    steps = input("Something went wrong! You can enter only a number\n")

in_text = input("Enter the text:\n")
while in_text.isspace():
    in_text = input("Something went wrong! Enter the text\n")

if lang == 'en':
    capacity = 26
    low_alphabet = eng_lower_alphabet
    upp_alphabet = eng_upper_alphabet

elif lang == 'ru':
    capacity = 32
    low_alphabet = rus_lower_alphabet
    upp_alphabet = rus_upper_alphabet


def encrypt(text, step):
    result = ''
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].islower():
                place = low_alphabet.index(text[i])
                result += low_alphabet[(place + int(step)) % capacity]
            elif text[i].isupper():
                place = upp_alphabet.index(text[i])
                result += upp_alphabet[(place + int(step)) % capacity]
        else:
            result += text[i]
    return print(f"The result: {result}")


def decrypt(text, step):
    result = ''
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].islower():
                place = low_alphabet.index(text[i])
                result += low_alphabet[(place - int(step)) % capacity]
            elif text[i].isupper():
                place = upp_alphabet.index(text[i])
                result += upp_alphabet[(place - int(step)) % capacity]
        else:
            result += text[i]
    return print(f"The result: {result}")


if action == 'e':
    encrypt(in_text, steps)
elif action == 'd':
    decrypt(in_text, steps)
