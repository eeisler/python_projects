import random

word_list = ['knee', 'knife', 'knock', 'adapt', 'know', 'affect', 'land', 'afford', 'lap', 'large', 'last', 'borrow',
             'map', 'margin', 'budget', 'mark', 'market', 'campus', 'nerve', 'civil', 'oppose', 'deal', 'porch', 'port',
             'pose', 'quit', 'elite', 'quote', 'recipe', 'email', 'emerge', 'refuse', 'regard', 'scope', 'score',
             'fiber', 'scream', 'screen', 'field', 'script', 'tactic', 'forest', 'tail', 'forget', 'form', 'talent',
             'formal', 'uncle', 'gear', 'gender', 'gene', 'video', 'view', 'viewer', 'holy', 'weapon', 'home', 'wear',
             'image', 'week', 'impact', 'year', 'income', 'yell', 'yellow', 'joy', 'judge', 'equal', 'lord', 'king',
             'france', 'cousin', 'will', 'move', 'speedy', 'friend', 'seem', 'make', 'denial', 'love', 'wisdom',
             'answer', 'mean', 'freely', 'leave', 'stand', 'part', 'well', 'serve', 'gentry', 'sick', 'enter', 'count',
             'good', 'young', 'youth', 'bear', 'father', 'face', 'frank', 'nature', 'haste', 'moral', 'paris', 'duty',
             'look', 'time', 'long', 'steal', 'talk', 'return', 'hide', 'honour', 'like', 'pride', 'clock', 'true',
             'minute', 'speak', 'tongue', 'obey', 'hand', 'place', 'proud', 'poor', 'praise', 'copy', 'follow', 'rich',
             'royal', 'speech', 'always', 'say', 'hear', 'word', 'ear', 'grow', 'live', 'begin', 'heel', 'flame',
             'lack', 'snuff', 'sense', 'expire', 'wish', 'honey', 'bring', 'home', 'hive', 'give', 'room', 'lend',
             'fill', 'know', 'month', 'rest', 'debate', 'stock', 'exchange', 'note', 'sell', 'equity', 'large',
             'liquid', 'attractive', 'guarantor', 'settlement', 'counter', 'dealer', 'different', 'attract', 'cover',
             'interest', 'frequently', 'likely', 'trade', 'transfer', 'money', 'security', 'seller', 'buyer', 'agree',
             'price', 'ownership', 'particular', 'company', 'market', 'range', 'small', 'individual', 'larger', 'world',
             'include', 'insurance', 'pension', 'hedge', 'trader', 'physical', 'floor', 'method', 'known', 'open',
             'offer', 'type', 'network', 'example', 'potential', 'specific', 'accept', 'match', 'sale', 'place',
             'multiple', 'purpose', 'facilitate', 'provide', 'real', 'discovery', 'hybrid', 'location', 'flow',
             'broker', 'order', 'post', 'maintain', 'spread', 'case', 'close', 'difference', 'tape', 'brokerage',
             'firm', 'investor', 'play', 'important', 'role', 'program', 'electronic', 'computer', 'similar',
             'purchase', 'drive', 'late', 'system']


def get_word():
    word = random.choice(word_list).upper()
    return word


def display_hangman(tries):
    stages = [
        r'''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / \
        |
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / 
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |     |
        |     |
        |     
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    
        |     
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     
        |    
        |       
        |  
        '''
    ]
    return stages[tries]


def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play the hangman game:)")
    print(display_hangman(tries))
    print(f'Word: {word_completion}\n')

    while not guessed and tries > 0:
        guess = input("Enter the letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already tried this letter', guess)
            elif guess not in word:
                print('Letter', guess, 'not in the word')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Great job, you guessed the letter')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You already answered with this word', guess)
            elif guess != word:
                print('Word', guess, 'is wrong')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Enter the letter')
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('You win!')
    else:
        print('You loose\nWord: ' + word)


again = 'y'

while again.lower() == 'y':
    word = get_word()
    play(word)
    again = input('Do you wanna play again? (y = yes, n = no):\n')
