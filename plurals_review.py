import random

hard_consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ш']
plural_exceptions = []
def make_plural_noun(word):

    if word[-1] in hard_consonants:
        print('plural form : ' + word + 'ы')
        print('Because it ends with hard consonants')
    elif word[-1] == 'a':
        print('plural form : ' + word[:-1:] + 'ы')
        print('Because it ends with a')

    elif word[-1] == 'я':
        print('plural form : ' + word[:-1:] + 'и')
        print('Because it ends with я')
    elif word[-1] == 'ь' or word[-1] == 'й':
        print('plural form : ' + word + 'и')
        if word[-1] == 'ь':
            print('Because it ends with ь')
        else:
            print('Because it ends with и')

    elif word[-1] == 'o':
        print('plural form : ' + word[:-1:] + 'a')
        print('Because it ends with o')
    elif word[-1] == 'e':
        print('plural form : ' + word[:-1:] + 'я')
        print('Because it ends with e')

    elif word in plural_exceptions:
        print('plural form : ' + word + 'и')
        print('Because it is exception')

    return 0

def guess_plural_noun(voca_dict):

    word_list = list(voca_dict.keys())
    asked_list = []
    max_idx = len(voca_dict) - 1
    print(max_idx)
    print('----------------------------------------------')
    print("I will give you a word. Answer it's plural form and why it is.")
    print("The word asked once will not be asked twice.\nif you want to stop, please type 'stop'")
    point = 0
    tries = 0

    while 1:
        idx = random.randint(0, max_idx)
        if idx in asked_list:
            continue
        word = word_list[idx]
        print("Guess the plural form : {}".format(word))
        _ = input()
        if _ == 'stop':
            break
        print("Answer : ")
        make_plural_noun(word)
        score_record = int(input("if you got answer type '1', if not type '0' : "))
        print('----------------------------------------------')
        while 1:
            score_record = int(input("if you got answer type '1', if not type '0' : "))
            print('----------------------------------------------')
            if score_record == 1:
                point += 1
                break
            elif score_record == 0:
                tries += 1
                break
            else:
                print("You pressed wrong key. Please input correct command")
                _ = input('Press any key to retry')

    print('number of questions was {} and you got {} points'.format(tries, point))
    print('----------------------------------------------')
    return 0

def plural_review(selected_voca, grammatical_vocabulary_book):

    global plural_exceptions

    plural_exceptions = (grammatical_vocabulary_book['plural_exceptions'].keys())
    voca_dict = selected_voca.update(grammatical_vocabulary_book)

    print('----------------------------------------------')
    print("Let's review the plural noun part.")
    while 1:
        print('select the course and press enter to start')
        print("0 = plural gender guess")
        print("quit = exit")
        select = input()
        if select == '0':
            guess_plural_noun(voca_dict)
        elif select == 'quit':
            _ = input('Are you done? y/n : ')
            if _ == 'y':
                break
        else:
            print("You pressed wrong key. Please input correct command")
            _ = input('Press any key to retry')

    return 0
