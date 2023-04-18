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

step = input("Enter shift step(number):\n")
while not step.isdigit():
    step = input("Something went wrong! You can enter only a number\n")

text = input("Enter the text:\n")
while text.isspace():
    text = input("Something went wrong! Enter the text\n")


def encrypt(text, lang, step):
    result = ''

    if lang == 'en':
        capacity = 26
        low_alphabet = eng_lower_alphabet
        upp_alphabet = eng_upper_alphabet

    elif lang == 'ru':
        capacity = 32
        low_alphabet = rus_lower_alphabet
        upp_alphabet = rus_upper_alphabet

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

    return print(result)


def decrypt(text, lang, step):
    pass


if action == 'e':
    encrypt(text, lang, step)
elif action == 'd':
    decrypt(text, lang, step)