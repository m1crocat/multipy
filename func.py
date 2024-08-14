current_version = "4.1.2"
version_date = "14.08.24"
from random import *
from time import *
from turtle import *
import os
import base64

def info():#я
    print(f"\nПрограмма MultiPy.\nВерсия {current_version} от {version_date}.\nТелеграмм разработчика - m1cro_cat\n")

def changelog():#я
    print(" Changelog")
    print(f">>{current_version} - {version_date}<<")
    print(">Багфикс\nЗначительная переделка функции линукс команд>")

def linux():
    q = int(input("Линукс команды\n1 - Установка софта через apt\n2 - apt\n3 - Системные команды\n0 - Выход\n\nВведите значение: "))
    print("\n")
    while q != 0:
        if q == 1:
                q = int(input("Установка разного софта\n*(может не работать на некоторых дистрибутивах)\n1 - Ввести свой пакет\n2 - firefox\n3 - vlc\n4 - obs-studio\n5 - gimp\n6 - vscode\n7 - telegram-desktop*\n8 - Thunderbird\n9 - steam*\n0 - Выход \n\nВведите значение: "))
                print("\n")
                while q != 0:
                    if q == 3:
                        print(os.system("""
                                        sudo install -d -m 0755 /etc/apt/keyrings && wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null && echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null && echo '
                                        Package: *
                                        Pin: origin packages.mozilla.org
                                        Pin-Priority: 1000
                                        ' | sudo tee /etc/apt/preferences.d/mozilla  && sudo apt-get update && sudo apt-get install firefox
                                        """))
                        print("\n")
                    elif q == 4:
                        print(os.system("sudo apt install vlc"))
                        print("\n")
                    elif q == 5:
                        print(os.system("sudo apt install obs-studio"))
                        print("\n")
                    elif q == 6:
                        print(os.system("sudo apt install gimp"))
                        print("\n")
                    elif q == 6:
                        print(os.system(""""
                                        sudo apt-get install wget gpg
                                        wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
                                        sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
                                        echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
                                        rm -f packages.microsoft.gpg
                                        sudo apt update && sudo apt install code
                                        """))
                        print("\n")
                    
                    elif q == 7:
                        print(os.system("sudo apt install telegram-desktop"))
                        print("\n")
                    elif q == 8:
                        print(os.system("sudo apt install thunderbird"))
                        print("\n")
                    elif q == 9:
                        print(os.system("sudo apt install steam"))
                        print("\n")
                    elif q == 1:
                        c = input("Введите пакет для установки: ")
                        print(os.system(f"sudo apt install {c}"))
                        print("\n")
                    else:
                        print("Введите корректное значение")
                        print("\n")
                q = int(input("Установка разного софта\n*(может не работать на некоторых дистрибутивах)\n1 - Ввести свой пакет\n2 - firefox\n3 - vlc\n4 - obs-studio\n5 - gimp\n6 - vscode\n7 - telegram-desktop*\n8 - Thunderbird\n9 - steam*\n0 - Выход \n\nВведите значение: "))
                print("\n")
        elif q == 2:
            q = int(input("apt команды\n1 - Своя команда\n2 - sudo apt update\n3 - sudo apt upgrade -y\n4 - sudo apt autoremove\n5 - update & upgrade -y\n0 - Выход \n\nВведите значение: "))
            print("\n")
            while q != 0:
                if q == 2:
                    print(os.system("sudo apt update"))
                    print("\n")
                elif q == 3:
                    print(os.system("sudo apt upgrade -y"))
                    print("\n")
                elif q == 4:
                    print(os.system("sudo apt autoremove"))
                    print("\n")
                elif q == 5:
                    print(os.system("sudo apt update && sudo apt upgrade -y"))
                    print("\n")
                elif q == 1:
                    c = input("Введите команду: ")
                    print(os.system(c))
                    print("\n")
                else:
                    print("Введите корректное значение")
                    print("\n")
                q = int(input("apt команды\n1 - Своя команда\n2 - sudo apt update\n3 - sudo apt upgrade -y\n4 - sudo apt autoremove\n5 - update & upgrade -y\n0 - Выход \n\nВведите значение: "))
                print("\n")
        elif q == 3:
            q = int(input("Системные команды\n1 - Своя команда\n2 - neofetch\n3 - uname -a\n0 - Выход \n\nВведите значение: "))
            print("\n")
            while q != 0:
                if q == 2:
                    print(os.system("neofetch "))
                    print("\n")
                elif q == 3:
                    print(os.system("uname -a"))
                    print("\n")
                elif q == 1:
                    c = input("Введите команду: ")
                    print(os.system(c))
                    print("\n")
                else:
                    print("Введите корректное значение")
                    print("\n")
                q = int(input("Системные команды\n1 - Своя команда\n2 - neofetch\n3 - uname -a\n0 - Выход \n\nВведите значение: "))
                print("\n")
        else:
            print("Введите корректное значение")
            print("\n")
        q = int(input("Линукс команды\n1 - Установка софта через apt\n2 - apt\n3 - Системные команды\n0 - Выход\n\nВведите значение: "))
        print("\n")
def convertor():#я
            ipt = input("Введите из чего в что вы хотите перевести \nДоступно: от мм до км, от байтов до тб\nНапример: байты - тб, метры - см\n(введите 0 для выхода): ").lower()
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
        spd = int(input("Введите скорость: "))
        def paint():
            # задаю цвет
            colormode(255)
            color1 = (randint(0, 255), randint(0, 255), randint(0, 255))
            color2 = (randint(0, 255), randint(0, 255), randint(0, 255))
            color(color1, color2)
            #скорость
            speed(spd)
            #поворот
            left(randint(1, 359))
            # генерация 
            pensize(randint(4, 12))
            cur1 = randint(10, 200)
            ran1 = randint(1,10)
            # рандомные координаты
            screensize(500, 500)
            penup()
            goto(randint(-500, 500), randint(-500, 500))
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
                pensize(randint(1, 10))
                for i in range(randint(10, 36)):
                    forward(per11)  
                    per11 += 5
                    left(90) 
            if ran1 == 7:
                # пончик
                speed(spd + 20)
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
            if ran1 == 8:
                # ромб
                rand = randint(50,150)
                if randint(1,2) == 1:
                    left(randint(0,360))
                    for i in range(2):
                        left(45)
                        forward(rand)
                        left(135)
                        forward(rand)
                else:
                    begin_fill()
                    left(randint(0,360))
                    for i in range(2):
                        left(45)
                        forward(rand)
                        left(135)
                        forward(rand)
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

def igraUgadaika():#я
    count1 = 1
    print("Угадайте число от 1 до 100! (Введите 0 если хотите сдаться)")
    count = randint(1,100)
    price = int(input("Введите число: "))
    while price != count:
        count1 += 1
        if price == 0:
            print("Число:", count)
            break
        elif price >= 101:
            print("Сказали же, ДО 100 xD")
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
    print(os.system(f"ping {i1}"))

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

def game_sherepash():
    def prnt(t):
        t.speed(30)
        t.penup()
        t.goto(-200, -200)
        t.pendown()
        for i in range(4):
            t.forward(400)
            t.left(90)
    def game(t, s):
        t1.onclick(clck1)
        t2.onclick(clck2)
        t3.onclick(clck3)
        t.forward(10)
        sleep(s)
    def setting(t, c, m):
        t.penup()
        t.goto(0,0)
        t.color(c)
        t.speed(5)
        t.shape("turtle")
        t.left(m)
    def clck1(x, y):
        t1.left(randint(1, 359))
        t1.goto(randint(-100, 100), randint(-100, 100))
    def clck2(x, y):
        t2.left(randint(1, 359))
        t2.goto(randint(-100, 100), randint(-100, 100))
    def clck3(x, y):
        t3.left(randint(1, 359))
        t3.goto(randint(-100, 100), randint(-100, 100))
    def gamefinish():
        if abs(t1.xcor()) >= 200 or abs(t1.ycor()) >= 200:
            if t1.xcor() >= -10:
                t1.setheading(180)
                t1.goto(-180, t1.ycor())
            t1.write("GAME OVER!", font=("Arial", 40, "italic"))
            return False
        elif abs(t2.xcor()) >= 200 or abs(t2.ycor()) >= 200:
            if t2.xcor() >= -10:
                t2.setheading(180)
                t2.goto(-180, t2.ycor())
            t2.write("GAME OVER!", font=("Arial", 40, "italic"))
            return False
        elif abs(t3.xcor()) >= 200 or abs(t3.ycor()) >= 200:
            if t3.xcor() >= -10:
                t3.setheading(180)
                t3.goto(-180, t3.ycor())
            t3.write("GAME OVER!", font=("Arial", 40, "italic"))
            return False
        else:
            return True
    spd = int(input("Привет! Какой уровень сложности от 1 до 3 ты хочешь выбрать? "))
    while spd:
        if spd == 1:
            spdgame = 0.2
            break
        elif spd == 2:
            spdgame = 0.1
            break
        elif spd == 3:
            spdgame = 0.01
            break
        elif spd == 4:
            spdgame = 0.0000001
            break
        else:
            print("Вы ввели недопустимый уровень :(")
            spd = int(input("Какой уровень сложности от 1 до 3 ты хочешь выбрать? "))
    t1 = Turtle()
    t2 = Turtle()
    t3 = Turtle()
    prnt(t1)
    setting(t1, "red", 0)
    setting(t2, "green", 120)
    setting(t3, "blue", 240)
    strt_time = time()
    while gamefinish():
        game(t1, spdgame)
        game(t2, spdgame)
        game(t3, spdgame)
    end_time = time()
    print("Вы набрали", int(end_time - strt_time), "баллов!")
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
