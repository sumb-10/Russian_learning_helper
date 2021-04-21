import Number_quiz
import pronounciation_quiz

def main_menu():

    print("Welcome to the " + '\033[97m' + "*" + '\033[94m' + "*" + '\033[91m' + "*" + '\033[97m' + " Russian" + '\033[94m' + " Learning" + '\033[91m' + " Helper" + '\033[97m' + " *" + '\033[94m' + "*" + '\033[91m' +"*" + '\033[0m' "!!")
    print("This program is based on the lecture of 'Tanya's Russian Class' and originated by Hojin Cho, University Of Seoul.\nThe last update(v.1.0) was 2021.04.21")
    _ = input('press any key to start')

    while 1:
        print('----------------------------------------------')
        print("Please select the course you want to study")
        print('0 = number_quiz')
        print('1 = pronounciation_quiz')
        print('quit = exit\n')

        select_course = input()
        if select_course == '0':
            Number_quiz.number_quiz()
            _ = input('press any key to back to main menu')
        if select_course == '1':
            pronounciation_quiz.alphabet_pronounciation_quiz()
            _ = input('press any key to back to main menu')
        if select_course == 'quit':
            _ = input("You want to quit? y/n : ")
            if _ == 'y':
                break
            _ = input('press any key to back to main menu')

    return 0

if __name__ == "__main__":
    main_menu()