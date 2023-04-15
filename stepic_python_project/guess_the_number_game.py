from random import randint

def is_valid_answer(num):
    if num.isdigit() and float(num) - int(float(num)) == 0 and 1 <= int(num) <= 100:
        return True
    else:
        return False

def start_game():
    print("This is GuessTheNumber game."
          "\nThe rules are simple:"
          "\nWe generate a random number in a range which you can choose and then you guess it. "
          "\nYou'll be given a hints if your number is bigger or smaller than the right answer"
          "\nEnter the range:")

    while True: #todo - after n in continue the game continues to work
        x, y = input(), input()
        if x.isdigit() and y.isdigit():
            if int(x) > int(y):
                x, y = y, x
        print(f"Guess the number between {x} and {y}: ")
        compare_numbers(x, y)

def compare_numbers(x, y):
    count = 1
    answer = randint(int(x), int(y))
    while True:
        user_answer = input()
        if is_valid_answer(user_answer) == True:
            if int(user_answer) > answer:
                print("Smaller")
                count += 1
            elif int(user_answer) < answer:
                print("Bigger")
                count += 1
            elif int(user_answer) == answer:
                print(f"You won! Count of tries: {count}")
                continue_game()
                break
        else:
            print("Incorrect number try again: ")
            continue
def continue_game():
    print("Do you wanna continue to play? y/n")
    user_answer = input()
    if user_answer in ("y", "n"):
        if user_answer == "y":
            start_game()
        elif user_answer == "n":
            print("See you later")
    else:
        print("Invalid command. Try again. y or n?")

start_game()