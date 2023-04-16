from random import randint

def is_valid_answer(num, x, y):
    if num.isdigit() and float(num) - int(float(num)) == 0 and x <= int(num) <= y:
        return True
    else:
        return False
def start_game():
    print("Hello! This is GuessTheNumber game.")
    while True:
        print("Enter the range to guess the number: ")
        x, y = input(), input()
        if x.isdigit() and y.isdigit():
            if int(x) > int(y):
                x, y = y, x
        print(f"Guess the number between {x} and {y}: ")
        compare_numbers(x, y)
        if continue_game():
            continue
        else:
            break
def compare_numbers(x, y):
    answer = randint(int(x), int(y))
    count = 1
    while True:
        user_answer = input()
        if is_valid_answer(user_answer, int(x), int(y)) == True:
            if int(user_answer) > answer:
                print("Smaller")
                count += 1
            elif int(user_answer) < answer:
                print("Bigger")
                count += 1
            elif int(user_answer) == answer:
                print(f"You won! Count of tries: {count}")
                break
        else:
            print("Incorrect number try again: ")
            continue
def continue_game():
    user_answer = input("Do you wanna continue to play? y/n\n")
    while True:
        if user_answer not in ("y", "n", "Y", "N"):
            user_answer = input("Invalid command. Try again. y or n?")
        elif user_answer in ("n", "N"):
            print("See you later")
            return False
        else:
            return True
start_game()