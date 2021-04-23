import random
number_dict_unit_digit = {0 : 'нуль', 1: 'один', 2 : 'два', 3 : 'три', 4 : 'четыре', 5 : 'пять', 6 : 'шесть', 7 : 'семь', 8 : 'восемь', 9 : 'девять' , 10 : 'десять' }
number_dict_eleven_to_nineteen = {10 : 'десять', 11 : 'одиннадцать', 12 : 'двенадцать', 13 : 'тринадцать', 14 : 'четырнадцать', 15 : 'пятнадцать', 16 : 'шестнадцать', 17 : 'семнадцать', 18 : 'восемнадцать', 19 : 'девятнадцать'}
number_dict_tens_digit = {0 : '', 1 : 'десять', 2 : 'двадцать', 3 : 'тридцать', 4 : 'сорок', 5 :'пятьдесят', 6 : 'шестьдесят', 7 :'семьдесят', 8 : 'восемьдесят', 9 : 'девяносто', 10 : 'сто'}
number_dict_hundreds_digit = {0 : '', 1 : 'сто', 2 : 'двести', 3 : 'триста', 4 : 'четыреста', 5 : 'пятьсот', 6 : 'шестьсот', 7 : 'семьсот', 8 : 'восемьсот', 9 : 'девятьсот', 10 : 'тысяча'}
number_dict_thousand_digit = {0 : 'тысяч', 1: 'одна тысяча', 2 : 'две тысячи', 3 : 'три тысячи', 4 : 'четыре тысячи', 5 : 'пять тысяч', 6 : 'шесть тысяч', 7 : 'семь тысяч', 8 : 'восемь тысяч', 9 : 'девять тысяч', 10 : 'десять тысяч'}

def find_answer(number):
    if number == 0:
        return 'нуль'
    elif number == 100:
        return 'сто'
    elif number == 1000:
        return 'тысяча'
    elif number == 1000000:
        return 'миллион'
    elif number in number_dict_unit_digit:
        return number_dict_unit_digit[number]
    elif number in number_dict_eleven_to_nineteen:
        return number_dict_eleven_to_nineteen[number]
    elif number in number_dict_tens_digit:
        return number_dict_tens_digit[number]
    else:
        number_divided_by_digit = []
        while number > 0:
            number_divided_by_digit.append(number % 10)
            number //= 10
        answer = ''

        for idx in range(len(number_divided_by_digit) - 1, -1, -1):
            if idx == 5:
                answer += ' ' + number_dict_hundreds_digit[number_divided_by_digit[idx]]
            if idx == 4:
                if number_divided_by_digit[idx] == 1:
                    answer += ' ' + number_dict_eleven_to_nineteen[number_divided_by_digit[idx]*10 + number_divided_by_digit[idx - 1]] + ' тысяч'
                elif number_divided_by_digit[idx] == 0:
                    pass
                else:
                    answer += ' ' + number_dict_tens_digit[number_divided_by_digit[idx]]
            if idx == 3:
                if len(number_divided_by_digit) > 4:
                    if number_divided_by_digit[idx + 1] == 1:
                        pass
                    else:
                        answer += ' ' + number_dict_thousand_digit[number_divided_by_digit[idx]]
                else:
                    answer += ' ' + number_dict_thousand_digit[number_divided_by_digit[idx]]
            if idx == 2:
                if number_divided_by_digit[idx] == 0:
                    pass
                else:
                    answer += ' ' + number_dict_hundreds_digit[number_divided_by_digit[idx]]
            if idx == 1:
                if number_divided_by_digit[idx] == 1:
                    answer += ' ' + number_dict_eleven_to_nineteen[number_divided_by_digit[idx]*10 + number_divided_by_digit[idx - 1]]
                elif number_divided_by_digit[idx] == 0:
                    pass
                else:
                    answer += ' ' + number_dict_tens_digit[number_divided_by_digit[idx]]
            if idx == 0:
                if len(number_divided_by_digit) > 1:
                    if number_divided_by_digit[idx + 1] == 1:
                        pass
                    else:
                        answer += ' ' + number_dict_unit_digit[number_divided_by_digit[idx]]
                else:
                    answer += ' ' + number_dict_unit_digit[number_divided_by_digit[idx]]

        return answer[1:]

def number_quiz():
    print('----------------------------------------------')

    print("recommanded courses :\n1 ~ 100\n100 ~ 1000\n1000 ~ 10000\n10000 ~ 1000000")
    print('----------------------------------------------')

    start = int(input("please input a start number(0~999999) : "))
    end = int(input("please input a end number(1~1000000) : "))
    print('----------------------------------------------')
    print("I will give you random number({} ~ {}) and you should translate it into russian.\nThe number asked once will not be asked twice.\nif you want to stop, please type 'stop'".format(start, end))
    print('----------------------------------------------')
    num_list = []
    point = 0
    tries = 0

    while 1:
        number = random.randint(start, end)
        if number in num_list:
            continue

        else:
            num_list.append(number)
            print("Translate the number : {}".format(number))
            _ = input()
            if _ == 'stop':
                break
            print("Answer:")
            print(find_answer(number))

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

    return 0