current_version = "4.1.1 lite"
version_date = "08.08.24"
from random import *
from time import *
from os import system
from os import name
import base64

def info():#я
    print(f"\nПрограмма MultiPy lite.\nВерсия {current_version} от {version_date}.\nТелеграм-канал программы - multipy_prog\nТелеграмм разработчика - m1cro_cat\n")

def changelog():#я
    print(" Changelog")
    print(f">>{current_version} - {version_date}<<")
    print(">Багфикс\n>Улучшение функции linux\n")


def linux():
    q = int(input("Линукс команды\n1 - Своя команда\n2 - neofetch\n3 - uname -a\n4 - sudo apt update\n5 - sudo apt upgrade -y\n6 - sudo apt autoremove\n7 - update & upgrade -y\n0 - Выход \n\nВведите значение: "))
    print("\n")
    while q != "0":
        if q == 2:
            print(system("neofetch "))
            print("\n")
        elif q == 3:
            print(system("uname -a"))
            print("\n")
        elif q == 4:
            print(system("sudo apt update"))
            print("\n")
        elif q == 5:
            print(system("sudo apt upgrade -y"))
            print("\n")
        elif q == 6:
            print(system("sudo apt autoremove"))
            print("\n")
        elif q == 7:
            print(system("sudo apt update && sudo apt upgrade -y"))
            print("\n")
        elif q == 1:
            c = input("Введите команду: ")
            print(system(c))
        elif q == 0:
            break
        else:
            print("Введите корректное значение")
            print("\n")
        q = int(input("Линукс команды\n1 - Своя команда\n2 - neofetch\n3 - uname -a\n4 - sudo apt update\n5 - sudo apt upgrade -y\n6 - sudo apt autoremove\n7 - update & upgrade -y\n0 - Выход \n\nВведите значение: "))
        print("\n")

def igraUgadaika():#я
    count1 = 1
    print("Угадайте число от 1 до 100! (Введите 0 если хотите сдаться)")
    count = randint(1,100)
    if randint(1,100) == 3:
        count = randint(5,20)**40
    price = int(input("Введите число: "))
    while price != count:
        count1 += 1
        if price == 0:
            print("Число:", count)
            break
        elif price >= 101:
            print("Сказали же, ДО 100 xD")
        elif count1 > 100:
            print("Вам с шансем 1% выпало число больше 100! Число", count)
        elif price > count and price != 0:
            print("Число меньше!")
        elif price < count :
            print("Число больше!")
        else:
            break
        price = int(input("Введите число: "))
    if price == count:
        print("Вы угадали!")
        print("Количество попыток:", count1)

def stopwatch():#инет\нейросеть
    print("Нажмите Enter чтобы начать, Ctrl+C чтобы остановить")
    try:
        input()
        start = perf_counter()
        while True:
            elapsed = perf_counter() - start
            hours = str(int(elapsed / 3600)).zfill(2)
            minutes = str(int(elapsed / 60) % 60).zfill(2) 
            seconds = str(int(elapsed) % 60).zfill(2)
            milliseconds = str(int(elapsed * 1000) % 1000).zfill(3)
            print("\r{0}:{1}:{2}:{3}".format(hours, minutes, seconds, milliseconds), end="")

    except KeyboardInterrupt:
        print("\nСекундомер остановлен!")

def timer():#инет\нейросеть
    try:
        my_time = int(input("Таймер обратного отсчета. Введите секунды: "))
        end = time() + my_time
        while time() < end:
            remaining = end - time()
            hours = int(remaining / 3600) 
            minutes = int(remaining / 60) % 60
            seconds = int(remaining) % 60
            milliseconds = int(remaining * 1000) % 1000
            
            print(f"\r{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:03}", end="")
            print("\r", end="")
            sleep(0.01)
                    
        print("\r\nВремя вышло!")
    except ValueError:
        print("Неправильное значение!")

def gen(): #частично я частично инет
    per1 = int(input("1 - генератор букв, 2 - генератор цифр, 3 - генератор пароля(буквы + цифры): "))
    if per1 == 1:
        per2 = ""
        passLength = int(input("Введите длину: "))
        # alph - это алфавит
        alphEn = "abcdefghijklmnopqrstuvwxyz"
        alphRu = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        lang = input("А какой язык? en / ru / all? ").lower()
        if lang == "ru":
            alph = alphRu
        if lang == "en":
            alph = alphEn
        if lang == "all":
            alph = ""
            alph += alphRu
            alph += alphEn
        for i in range(passLength):
            per2 += alph[randint(0, (len(alph) - 1))]
        print(per2)
    if per1 == 2:
        passLength = int(input("Введите длину: "))
        per1 = ""
        for i in range(passLength):
            per1 += str(randint(0,9))
        print(per1)
    if per1 == 3:
        password = ""
        passLength = int(input("Введите длину: "))
        alph = 'ABCDEFGHIJKLANOPQRSTUVWXYZabcdefghijklanopqrstuvwxyz123456789~!@#$%^&*()-_+=|/:;"<,>.?/' #thks to rodion
        for i in range(passLength):
            password += alph[randint(0, 81)]
        print(password)

def base64fun():#интернет
    q = int(input("1 - зашифровать, 2 - расшифровать: "))
    if q == 2:
        encoded_string = input("Введите строку для расшифрования: ")
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode("utf-8")
        print(decoded_string)
    if q == 1:
        q = input("Введите строку для шифрования: ")
        b = q.encode("UTF-8")
        e = base64.b64encode(b)
        s1 = e.decode("UTF-8")
        print(s1)

def length():#я
    per3 = input("Введите строку: ")
    print("Длина строки:", len(per3))

def ping():#я
    i1 = input("Введите ip, или доменное имя для пинга (или укажите параметр -t на windows, если надо пинговать бесконечно): ")
    print(system(f"ping {i1}"))

def knb():#я
    response = int(input("Камень(1), ножницы(2), или бумага?(3) (0 - выход): "))
    point_user = 0
    point_prog = 0
    while response != 0:
        randomAnswer = randint(1,3)
        if randomAnswer == 1 and response == 1:
            per1 = "Камень, ничья!"
        if randomAnswer == 1 and response == 2:
            per1 = "Камень, я победил!"
            point_prog += 1
        if randomAnswer == 1 and response == 3:
            per1 = "Камень, ты победил!"
            point_user += 1
        if randomAnswer == 2 and response == 1:
            per1 = "Ножницы, ты победил!"
            point_user += 1
        if randomAnswer == 2 and response == 2:
            per1 = "Ножницы, ничья!"
        if randomAnswer == 2 and response == 3:
            per1 = "Ножницы, я победил!"
            point_prog += 1
        if randomAnswer == 3 and response == 1:
            per1 = "Бумага, я победил!"
            point_prog += 1
        if randomAnswer == 3 and response == 2:
            per1 = "Бумага, ты победил!"
            point_user += 1
        if randomAnswer == 3 and response == 3:
            per1 = "Бумага, ничья!"
        print(per1)
        response = int(input("Камень(1), ножницы(2), или бумага?(3) (0 - выход): "))
        if point_prog >= 3:
                print("Ты проиграл!")
                break
        if point_user >= 3:
                print("Ты победил!")
                break

