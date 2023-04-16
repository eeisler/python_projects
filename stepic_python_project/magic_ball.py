from random import randint, choice

answer_list = ["Definitely", "Determined", "No doubt", "Definitely yes", "You can be sure of it",
               "I think yes", "Most likely", "Good prospects", "Signs say yes" , "Yes",
               "Unclear yet, try again", "Ask later", "Better not tell", "Can't predict now", "Concentrate and ask again",
               "Don't even think", "My answer is no", "According to my information, no", "Prospects are not very good", "Very doubtful"]
ask_question_list = ["What is your question?", "What question is bothering you, my friend?", "What do you want to know?",
                     "You came to me with a question, for your future is vague. Ask a question and you will get an answer."]


def greetings():
    print("Hello, my curious friend, I am a magic ball and I know the answer to any of your questions.")
    user_name = input("But first, let me know your name\n")
    print(f"Hm.. {user_name}.. What a beautiful name)")
    game()


def game():
    while True:
        question = input(f"{choice(ask_question_list)}\n")
        print(choice(answer_list))
        if not continue_game(): break


def continue_game():
    answer = input("Do you want to know something else, my friend?\n")
    while True:
        if answer.lower not in ("no", "n", "not really",
                      "yes", "y", "yes please"):
            answer = input("I don't understand you...Try to repeat, please\n")
        if answer.lower() in ("no", "n", "not really"):
            print("Well then, see you later!")
            return False
        else:
            return True


greetings()
