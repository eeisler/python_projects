from random import *

def is_valid_answer(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False

print("Hello! This is GuessTheNumber game."
      "\nThe rules are simple:"
      "\n\tWe generate a random number and you should guess it. "
      "\n\tYou'll be given a hints if your number is bigger or smaller than the right answer"
      "\nDo you wanna play by yourself(1) or just watch how algorithm do it for you(2)?"
      "\nEnter the command: ")

command = int(input())

if command == 1:
    answer = randint(1, 100)
    print("Guess the number between 1 and 100: ")
    while True:
        user_answer = input()
        if is_valid_answer(user_answer) == True:
            if int(user_answer) > answer:
                print("Smaller")
                continue
            elif int(user_answer) < answer:
                print("Bigger")
                continue
            elif int(user_answer) == answer:
                print("You won!")
                break
        else:
            print("Incorrect number try again: ")
            continue

if command == 2:
    answer = randint(1, 100)
    left, right = 1, 100
    guessing = (left + right) // 2
    count = 0
    while guessing != answer:
        if guessing < answer:
            print(f"Guessing is: {guessing}")
            print("Smaller")
            left = guessing + 1
            guessing = (left + right) // 2
            count += 1
        elif guessing > answer:
            print(f"Guessing is: {guessing}")
            print("Bigger")
            right = guessing - 1
            guessing = (left + right) // 2
            count += 1
    print(f"The answer is: {guessing}"
          f"\nCount of tries: {count}")