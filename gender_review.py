import random

consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
feminine_nouns = []
masculine_nouns = []
neutral_nouns = []
feminine_nouns_ends_with_soft_sign = []
masculine_nouns_ends_with_soft_sign = []
gender_exception = {}

def analyze_noun_gender(word):

    if word in feminine_nouns:
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a feminine noun(Женский род)')
    elif word in masculine_nouns:
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a masculine noun(Мужской род)')
    elif word in neutral_nouns:
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a neutral noun(Средний род)')
    elif word[-1] in consonants:
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a masculine noun(Мужской род)')
        print("Because it ends with 'consonants letter'")
    if word[-1] == 'а' or word[-1] == 'я':
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a feminine noun(Женский род)')
        if word[-1] == 'а':
            print("Because it ends with 'a'")
        else:
            print("Because it ends with 'я'")
    elif word[-1] == 'о' or word[-1] == 'е':
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a neutral noun(Средний род)')
        if word[-1] == 'о':
            print("Because it ends with 'o'")
        else:
            print("Because it ends with 'e'")
    elif word[-1] == 'ь':
        if word[:-2] in feminine_nouns_ends_with_soft_sign:
            print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a feminine noun(Женский род)')
            print("Because it is ends with '{}'".format(word[:-2]))
        elif word[:-3] == 'сть':
            print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a feminine noun(Женский род)')
            print("Because it is ends with 'сть'")

        if word[-4:] == 'тель':
            print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a feminine noun(Женский род)')
            print("Because it is ends with 'тeль'")
        elif word[-3:] == 'арь':
            print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a feminine noun(Женский род)')
            print("Because it is ends with 'apь'")

    return 0

def noun_gender_quiz(voca_dict):
    word_list = list(voca_dict.keys())
    asked_list = []
    max_idx = len(voca_dict) - 1
    print(max_idx)
    print('----------------------------------------------')
    print("I will give you a word. Answer if it is feminine or masuculine or neutral and why it is.")
    print("The word asked once will not be asked twice.\nif you want to stop, please type 'stop'")
    point = 0
    tries = 0

    while 1:
        idx = random.randint(0, max_idx)
        if idx in asked_list:
            continue
        word = word_list[idx]
        print("Guess the gender : {}".format(word))
        _ = input()
        if _ == 'stop':
            break
        print("Answer : ")
        analyze_noun_gender(word)
        score_record = int(input("if you got answer type '1', if not type '0' : "))
        print('----------------------------------------------')
        if score_record:
            point += 1
        tries += 1

    print('number of questions was {} and you got {} points'.format(tries, point))
    return 0

def noun_gender_guess():
    print('----------------------------------------------')
    print("Write down the noun. I will figure out it's gender. if you want to quit, type stop")
    print("The guess is only figured out by the database, so please search it on the internet. It could be wrong")

    while 1:
        word = input("Write down the noun : ")
        if word == 'stop':
            print('----------------------------------------------')
            break
        else:
            _ = input()
            analyze_noun_gender(word)
            print('----------------------------------------------')

    return 0

def gender_review(voca_dict):
    print('----------------------------------------------')
    print("Let's review the gender part.")
    while 1:
        print('select the course and press enter to start')
        print("0 = noun gender quiz")
        print("1 = noun gender guess")
        print("quit = exit")
        select = input()
        if select == '0':
            noun_gender_quiz(voca_dict)
        elif select == '1':
            noun_gender_guess()
        elif select == 'quit':
            _ = input('Are you done? y/n : ')
            if _ == 'y':
                break

    return 0
