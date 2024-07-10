current_version = "4.0.0"
version_date = "10.07.24"


from random import *
from time import *
from turtle import *
import os
import base64


def prt():#я
        print()
    #
def convertor():#я
            ipt = input("Введите из чего в что вы хотите перевести \nДоступно: все от мм до км, все от байтов до тб\nНапример: байты - тб, метры - см\n(введите 0 для выхода): ").lower()
            while ipt != "0":
                # мм
                if ipt == "мм - см":
                    per1 = int(input("Введите мм: "))
                    print("Результат:", per1 / 10)
                elif ipt == "мм - дм":
                    per1 = int(input("Введите мм: "))
                    print("Результат:", per1 / 100)
                elif ipt == "мм - метры":
                    per1 = int(input("Введите мм: "))
                    print("Результат:", per1 / 1000)
                elif ipt == "мм - км":
                    per1 = int(input("Введите мм: "))
                    print("Результат:", per1 / 10000)
                # см
                elif ipt == "см - мм":
                    per1 = int(input("Введите см: "))
                    print("Результат:", per1 * 10)
                elif ipt == "см - дм":
                    per1 = int(input("Введите см: "))
                    print("Результат:", per1 / 10)
                elif ipt == "см - метры":
                    per1 = int(input("Введите см: "))
                    print("Результат:", per1 / 100)
                elif ipt == "см - км":
                    per1 = int(input("Введите см: "))
                    print("Результат:", per1 / 1000)
                # дм
                elif ipt == "дм - мм":
                    per1 = int(input("Введите дм: "))
                    print("Результат:", per1 * 100)
                elif ipt == "дм - см":
                    per1 = int(input("Введите дм: "))
                    print("Результат:", per1 * 10)
                elif ipt == "дм - метры":
                    per1 = int(input("Введите дм: "))
                    print("Результат:", per1 / 10)
                elif ipt == "дм - км":
                    per1 = int(input("Введите дм: "))
                    print("Результат:", per1 / 100)
                # метры
                elif ipt == "метры - мм":
                    per1 = int(input("Введите метры: "))
                    print("Результат:", per1 * 1000)
                elif ipt == "метры - см":
                    per1 = int(input("Введите метры: "))
                    print("Результат:", per1 * 100)
                elif ipt == "метры - дм":
                    per1 = int(input("Введите метры: "))
                    print("Результат:", per1 * 10)
                elif ipt == "метры - км":
                    per1 = int(input("Введите метры: "))
                    print("Результат:", per1 / 10)
                # км
                elif ipt == "км - мм":
                    per1 = int(input("Введите км: "))
                    print("Результат:", per1 * 10000)
                elif ipt == "км - см":
                    per1 = int(input("Введите км: "))
                    print("Результат:", per1 * 1000)
                elif ipt == "км - дм":
                    per1 = int(input("Введите км: "))
                    print("Результат:", per1 * 100)
                elif ipt == "км - метры":
                    per1 = int(input("Введите км: "))
                    print("Результат:", per1 * 10)

                # байты
                if ipt == "байты - кб":
                    per1 = int(input("Введите байты: ")) 
                    print("Результат:", per1 / 1024)
                elif ipt == "байты - мб":
                    per1 = int(input("Введите байты: "))
                    print("Результат:", per1 / 1024**2)  
                elif ipt == "байты - гб":
                    per1 = int(input("Введите байты: "))
                    print("Результат:", per1 / 1024**3)
                elif ipt == "байты - тб":
                    per1 = int(input("Введите байты: "))
                    print("Результат:", per1 / 1024**4)

                # кб
                elif ipt == "кб - байты":
                    per1 = int(input("Введите кб: "))
                    print("Результат:", per1 * 1024)

                elif ipt == "кб - мб":
                    per1 = int(input("Введите кб: "))
                    print("Результат:", per1 / 1024)

                elif ipt == "кб - гб":
                    per1 = int(input("Введите кб: "))
                    print("Результат:", per1 / 1024**2)

                elif ipt == "кб - тб":
                    per1 = int(input("Введите кб: "))
                    print("Результат:", per1 / 1024**3)


                # мб  
                elif ipt == "мб - байты":
                    per1 = int(input("Введите мб: "))
                    print("Результат:", per1 * 1024**2)

                elif ipt == "мб - кб":
                    per1 = int(input("Введите мб: "))
                    print("Результат:", per1 * 1024)

                elif ipt == "мб - гб":
                    per1 = int(input("Введите мб: "))
                    print("Результат:", per1 / 1024)

                elif ipt == "мб - тб":
                    per1 = int(input("Введите мб: "))
                    print("Результат:", per1 / 1024**2)


                # гб
                elif ipt == "гб - байты":
                    per1 = int(input("Введите гб: "))
                    print("Результат:", per1 * 1024**3)

                elif ipt == "гб - кб":
                    per1 = int(input("Введите гб: "))
                    print("Результат:", per1 * 1024**2) 

                elif ipt == "гб - мб":
                    per1 = int(input("Введите гб: "))
                    print("Результат:", per1 * 1024)

                elif ipt == "гб - тб":
                    per1 = int(input("Введите гб: "))
                    print("Результат:", per1 / 1024)


                # тб
                elif ipt == "тб - байты":
                    per1 = int(input("Введите тб: "))
                    print("Результат:", per1 * 1024**4)

                elif ipt == "тб - кб":
                    per1 = int(input("Введите тб: "))
                    print("Результат:", per1 * 1024**3)

                elif ipt == "тб - мб":
                    per1 = int(input("Введите тб: ")) 
                    print("Результат:", per1 * 1024**2)

                elif ipt == "тб - гб":
                    per1 = int(input("Введите тб: "))
                    print("Результат:", per1 * 1024)

def paintgpt():#полностью я
    try:
        def paint():
            # задаю цвет
            colormode(255)
            color1 = (randint(0, 255), randint(0, 255), randint(0, 255))
            color2 = (randint(0, 255), randint(0, 255), randint(0, 255))
            color(color1, color2)
            #скорость
            speed(10)
            # генерация 
            pensize(randint(4, 10))
            cur1 = randint(10, 200)
            ran1 = randint(1,10)
            # рандомные координаты
            penup()
            goto(randint(-250, 250), randint(-250, 250))
            pendown()
            if ran1 == 2:
                # звезда
                begin_fill()
                for i in range(5):
                    forward(150)
                    left(144)
                end_fill()
            if ran1 == 3:
                # квадрат 1
                if randint(1,2) == 1:
                    begin_fill()
                    for i in range(4):
                        forward(100)
                        left(90)
                    end_fill()
                else:
                    for i in range(4):
                        forward(100)
                        left(90)
            if ran1 == 4:
                # круг 2
                if randint(1,2) == 1:
                    begin_fill()
                    circle(cur1)
                    end_fill()
                else:
                    circle(cur1)
            if ran1 == 5:
                # треугольник
                if randint(1,2) == 1:
                    begin_fill()
                    for i in range(3):
                        forward(cur1)
                        left(120)
                    end_fill()
                else:
                    for i in range(3):
                        forward(cur1)
                        left(120)
            if ran1 == 6:
                # спираль
                per11 = 0
                for i in range(randint(10, 36)):
                    forward(per11)  
                    per11 += 5
                    left(90) 
            if ran1 == 7:
                # пончик
                speed(15)
                r = randint(0, 255)
                g = randint(0, 255)
                b = randint(0, 255)
                color2 = (r, g, b)
                for i in range(18):
                    color(color1)
                    forward(100)
                    left(120)
                    left(10)
                    color(color2)
                    forward(100)
                    left(120)
                    left(10) 
                    speed(10)
            if ran1 == 8:
                # ромб
                if randint(1,2) == 1:
                    ran2 = randint(50,150)
                    left(randint(0,360))
                    for i in range(2):
                        left(45)
                        forward(ran2)
                        left(135)
                        forward(ran2)
                else:
                    begin_fill()
                    ran2 = randint(50,150)
                    left(randint(0,360))
                    for i in range(2):
                        left(45)
                        forward(ran2)
                        left(135)
                        forward(ran2)
                    end_fill()
            if ran1 == 9:
                # шестиугольник
                ran2 = randint(50,150)
                if randint(1,2) == 1:
                    for i in range(6):
                        forward(ran2)
                        left(60)
                else:
                    ran2 = randint(50,150)
                    begin_fill()
                    for i in range(6):
                        forward(ran2)
                        left(60)
                    end_fill()
            if ran1 == 10:
                for i in range(25):
                    forward(10)
                    left(25)
        while True:
            paint()
    except Exception:
                print("PaintGPT закрыт")

def info():#я
    print(f"\nПрограмма MultiPy.\nВерсия {current_version} от {version_date}.")

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
        elif price < count:
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

def bench():#я(идея моя)
     input("Для начала теста нажмите Enter: ")
     time_st = time()
     sleep(5)
     time_end = time()
     print("Результат теста:", (time_end - time_st) - 5, "сек. время вычислений")


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
        passLength = int(input("Введите длину пароля: "))
        per1 = ""
        for i in range(passLength):
            per1 += str(randint(0,9))
        print(per1)
    if per1 == 3:
        per2 = ""
        passLength = int(input("Введите длину: "))
        alphEn = "abcdefghijklmnopqrstuvwxyz"
        alphRu = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        lang = input("А какой язык? en / ru / all? ").lower()
        if lang == "ru":
            alph = alphRu
        elif lang == "en":  
            alph = alphEn
        elif lang == "all":
            alph = "" 
            alph += alphRu
            alph += alphEn
        for i in range(passLength):
            per2 += alph[randint(0, len(alph)-1)]
            if randint(1,3) == 1:
                for i in range(randint(1, 3)):
                    per2 += str(randint(0,9))
        if len(per2) > passLength:
            per2 = per2[:passLength]
        print(per2)

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
    print(os.system(f"ping {i1}"))

def changelog():#я
    print("\nЛист обновлений!\n")
    print("4.0.0 - 10.07.24")

def knb():#я
    response = int(input("Камень(1), ножницы(2), или бумага?(3) (0 - выход, если вы обиделись введите 4): "))
    while response != 0:
        randomAnswer = randint(1,3)
        if randomAnswer == 1 and response == 1:
            per1 = "Камень, ничья!"
        if randomAnswer == 1 and response == 2:
            per1 = "Камень, я победил!"
        if randomAnswer == 1 and response == 3:
            per1 = "Камень, ты победил!"
        if randomAnswer == 2 and response == 1:
            per1 = "Ножницы, ты победил!"
        if randomAnswer == 2 and response == 2:
            per1 = "Ножницы, ничья!"
        if randomAnswer == 2 and response == 3:
            per1 = "Ножницы, я победил!"
        if randomAnswer == 3 and response == 1:
            per1 = "Бумага, я победил!"
        if randomAnswer == 3 and response == 2:
            per1 = "Бумага, ты победил!"
        if randomAnswer == 3 and response == 3:
            per1 = "Бумага, ничья!"
        elif response == 4:
            print("Игра закончена, вы победили и получаете шоколадную медальку! :3")
            break
        print(per1)
        response = int(input("Камень(1), ножницы(2), или бумага?(3) (0 - выход, если вы обиделись введите 4): "))
