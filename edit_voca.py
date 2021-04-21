import os

vocas_path = './vocas'

def write_new_voca_note():
    title = input("Write the title of voca note : ")
    f = open(vocas_path + '/' + title +'.py', 'w')
    print('Write down the word you want to add. Please use the next form. [Word] : [meaning]')
    print('If it is done, write down [quit] and press enter key to finish')
    print('If you want to miswrite write down ! and press enter key to rewrite')
    print('----------------------------------------------')

    while 1:
        writeline = input()
        if writeline.lower() == 'quit':
            end_check = input('Are you done? y/n : ')
            if end_check == 'y':
                break

        rewrite_signal = list(writeline)
        if '!' in rewrite_signal:
            rewrite_check = input('Will you rewrite? y/n : ')
            if rewrite_check == 'y':
                continue
        word, meaning = writeline.split(' : ')
        f.write(word + '\n')
        f.write(meaning + '\n')
    f.close

    return 0


def add_new_vocas():
    title = input("Write the title of voca note : ")
    f = open(vocas_path + '/' + title + '.py', 'a')
    print('Write down the word you want to add. Please use the next form. [Word] : [meaning]')
    print('If it is done, write down [quit] and press enter key to finish')
    print('If you want to miswrite write down ! and press enter key to rewrite')
    print('----------------------------------------------')

    while 1:
        writeline = input()
        if writeline.lower() == 'quit':
            end_check = input('Are you done? y/n : ')
            if end_check == 'y':
                break

        rewrite_signal = list(writeline)
        if '!' in rewrite_signal:
            rewrite_check = input('Will you rewrite? y/n : ')
            if rewrite_check == 'y':
                continue
        word, meaning = writeline.split(' : ')
        f.write(word + '\n')
        f.write(meaning + '\n')
    f.close

    return 0

def edit_vocas():
    while 1:
        print('press 0 to write new voca note')
        print('press 1 to add new vocas in a voca note')
        print('write down [quit] to go back to previous menu\n')

        _ = input()
        if _ == '0':
            write_new_voca_note()
        if _ == '1':
            add_new_vocas()
        if _ == 'quit':
            break
        else:
            print('please write down properly')
        print('----------------------------------------------')

    return 0


