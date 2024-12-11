#импорт
from random import randint
from time import sleep, time, perf_counter
from turtle import forward, left, end_fill, begin_fill, color, colormode, speed, pensize, goto, penup, pendown, circle, screensize, Turtle, Terminator
from os import name, system, path, remove
from sys import executable, argv, exit
from base64 import b64decode, b64encode
from json import dump, load
from subprocess import call
import turtle
#стабильные переменные
current_version = "4.2.3 stable"
version_date = "11.12.24"
slogan = "\n да"
prnt_unix = " 1 - Утилиты\n 2 - Игры\n 3 - О программе\n 4 - Список изменений\n 5 - Linux\n 6 - Настройки\n\n 0 - Выход"
prnt_other = " 1 - Утилиты\n 2 - Игры\n 3 - О программе\n 4 - Cписок изменений\n 5 - Настройки\n\n 0 - Выход"
defaultConfig = {"setup": False, "tips": False, "show_errors": False}
if name == "posix":
    prnt = prnt_unix 
else: 
    prnt = prnt_other
clear_command = "clear"
config_path = path.join(path.dirname(path.abspath(__file__)), "config.json")
framework_path = path.join(path.dirname(path.abspath(__file__)), "framework")
#жизненно важные функции
def openConfig():
    while True:
        if not path.isfile(config_path):
            q = input("Файл конфигурации не найден. \nХотите его восстановить и пройти настройку? \nВведите y если да, r если без настройки: ")
            if q == "y":
                with open(config_path, 'w') as file:
                    dump(defaultConfig, file, indent=4)
                with open(config_path, 'r') as file:
                    return load(file)
                setup()
                break
            if q == "r":
                with open(config_path, 'w') as file:
                    dump(defaultConfig, file, indent=4)
                with open(config_path, 'r') as file:
                    return load(file)
                break
        else:
            with open(config_path, 'r') as file:
                return load(file)
            break
config = openConfig()
def c(q = clear_command):
    if name == "posix":
        system(f"{q} 2>/dev/null")
    else:
        system(f"{q} 2>nul")
def d(func):
    def wrapper():
        while True:
            try:
                if not config.get("show_errors"):
                    c()
                    func()
                    c()
                    break
                if config.get("show_errors"):
                    func()
                    break
            except KeyboardInterrupt:
                print("\nЗакрыто\n")
                break
            except ValueError:
                print("Неправильное значение. Попробуйте снова.")
            except FileNotFoundError:
                print("Файл не найден. Переустановите программу.")
                break
            except Terminator:
                print("PaintGPT закрыт")
                break
            except Exception as e:
                print(f"Произошла ошибка: {e}. Обратитесь к разработчику.")
                break
    return wrapper

@d
def mpy():
    print(f""" 
 m    m m    m m     mmmmmmm mmmmm  mmmmm m     m
 ##  ## #    # #        #      #    #   "# "m m" 
 # ## # #    # #        #      #    #mmm#"  "#"  
 # "" # #    # #        #      #    #        #   
 #    # "mmmm" #mmmmm   #    mm#mm  #        #   {current_version} by m1cro_cat
 {slogan}
""")
    print(prnt)
    ipt = int(input("\nВыберите действие: "))
    while ipt != 0:
        if ipt == 1:
            one()
        elif ipt == 2:
            two()
        elif ipt == 3:
            info()
        elif ipt == 4:
            changelog()
        elif ipt == 5 and name == "posix":
            linux()
        elif ipt == 5 and name == "nt":
            settings()
        elif ipt == 6:
            settings()
        elif ipt == 123:
            debug()
        elif ipt == 0:
            break
        else:
            print("Введите корректное значение")
        print(prnt)
        ipt = int(input("\nВыберите значение: "))
def saveDumpConfig(a, b):
    try:
        config[a] = b
        with open(config_path, 'w') as file:
                dump(config, file, indent=4)
    except ValueError:
        print("Неправильное значение.")
    except FileNotFoundError:
        print("Файл не найден. Переустановите программу.")
    except Exception as e:
        print(f"Произошла ошибка: {e}. Обратитесь к разработчику.") 

#settings, setup и около того
@d
def restoreDefaultSettings():
    saveDumpConfig("tips", False)
    saveDumpConfig("show_errors", False)
@d
def setupReboot():
    saveDumpConfig("setup", True)
    reboot() 
@d
def setup():
    restoreDefaultSettings()
    q = input("Добро пожаловать в MultiPy\nДавайте пройдем настроку, чтобы вам было удобнее использовать программу.\nНажмите Enter чтобы продолжить: ")
    if q == "bypass":
        saveDumpConfig("setup", False)
        reboot()
    # c()
    q = int(input("Подсказки - эта функция поможет вам проще использовать программу.\nПодсказки будут вам говорить подробнее, что делать.\nВведите 1 если хотите включить, или 0 если не нужно: "))
    if q == 1:
        saveDumpConfig("tips", True)
    # c()
    q = int(input("Отладка - эта функция поможет вам лучше узнать, что вызывает ошибку.\nЕсли вы не разбираетесь в python, не рекомендуем ее включать.\nВведите 1 если хотите включить, или 0 если не нужно: "))
    if q == 1:
        saveDumpConfig("show_errors", True)
    # c()
    saveDumpConfig("setup", False)
    print("Настройка завершена! Перезапуск...")
    sleep(1)
    reboot()
@d
def settings():
    i = int(input(f"Настройки{'\nВведите цифру чтобы изменить значение на противоположное' if config.get('tips') else ''}\n1 - Отображение ошибок - {config.get("show_errors")}\n2 - Подсказки - {config.get("tips")}\n3 - Сброс настроек\n0 - Выход\nВведите значение: "))
    if i == 1:
        if config.get("show_errors"):
            saveDumpConfig("show_errors", False)
            reboot()
        else:
            saveDumpConfig("show_errors", True)
            reboot()
    elif i == 2:
        if config.get("tips"):
            saveDumpConfig("tips", False)
            reboot()
        else:
            saveDumpConfig("tips", True)
            reboot()
    elif i == 3:
        # c()
        q = input("Вы ТОЧНО хотите сбросить все настройки на заводские (все выключено)?\nВведите y если хотите, n или 0 если нет, и s если хотите начать первоначальную настроку.\nПути назад уже не будет!\nВведите значение: ")
        if q == "y":
            restoreDefaultSettings()
            reboot()
        elif q == "s":
            setupReboot()
@d
def reboot(): # 
    try:
       call([executable] + argv)
    finally:
        exit()
@d
def debug():
    q = int(input("Дебаг меню\n1 - Удалить конфигфайл\n2 - Перезапустить\n3 - Открыть setup\n4 - Запустить restoreDefaultSettings\n5 - openConfig\nВведите значение: "))
    while q != "":
        if q == 1:
            remove(config_path)
        elif q == 2:
            reboot()
        elif q == 3:
            setup()
        elif q == 4:
            restoreDefaultSettings()
        elif q == 5:
            openConfig()
        q = int(input("Дебаг меню\n1 - Удалить конфигфайл\n2 - Перезапустить\n3 - Открыть setup\n4 - Запустить restoreDefaultSettings\nВведите значение: "))
#основные функции по списку
@d
def changelog():#я
    print(" Changelog")
    print(f">>{current_version} - {version_date}<<")
    print(">>Багфикс установщика<<.")
    input("\n\nНажмите Enter чтобы продолжить. ") 
@d
def info():#я
    input(f"\nПрограмма MultiPy.\nВерсия {current_version} от {version_date}.\nТелеграмм разработчика - m1cro_cat\n\nНажмите Enter чтобы продолжить. ") 

#one
@d
def one():
    print(" 1 - Секундомер\n 2 - Таймер\n 3 - Генератор\n 4 - Base64\n 5 - Узнать длинну строки\n 6 - Ping\n 7 - Перевод строки наоборот\n 8 - To-Do лист \n 0 - Назад")
    ipt = int(input("\nВыберите действие: "))
    while ipt != 0:
        if ipt == 1:
            stopwatch()
        elif ipt == 2:
            timer()
        elif ipt == 3:
            gen()
        elif ipt == 4:
            base64fun()
        elif ipt == 5:
            length()
        elif ipt == 6:
            ping()
        elif ipt == 7:
            nazad()
        elif ipt == 8:
            todo()
        elif ipt == 0:
            break
        else:
            print("Введите корректное значение")
        print(" 1 - Секундомер\n 2 - Таймер\n 3 - Генератор\n 4 - Base64\n 5 - Узнать длинну строки\n 6 - Ping\n 7 - Перевод строки наоборот\n 8 - To-Do лист \n 0 - Назад")
        ipt = int(input("\nВыберите действие: "))
@d
def stopwatch():#инет\нейросеть
        print("Нажмите Enter чтобы начать, Ctrl+C чтобы остановить")
        input()
        start = perf_counter()
        while True:
            elapsed = perf_counter() - start
            hours = str(int(elapsed / 3600)).zfill(2)
            minutes = str(int(elapsed / 60) % 60).zfill(2) 
            seconds = str(int(elapsed) % 60).zfill(2)
            milliseconds = str(int(elapsed * 1000) % 1000).zfill(3)
            print("\r{0}:{1}:{2}:{3}".format(hours, minutes, seconds, milliseconds), end="")
        input("\n\nНажмите Enter чтобы продолжить. ")
@d
def timer():#инет\нейросеть
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
        input("\n\nНажмите Enter чтобы продолжить. ")
@d
def gen(): #я
    per1 = int(input(f"1 - Генератор букв\n2 - Генератор цифр\n3 - генератор пароля(буквы + цифры)\nВведите значение: "))
    if per1 == 1:
        # c()
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
        input("\n\nНажмите Enter чтобы продолжить: ")
    if per1 == 2:
        # c()
        passLength = int(input("Введите длину: "))
        per1 = ""
        for i in range(passLength):
            per1 += str(randint(0,9))
        print(per1)
        input("\n\nНажмите Enter чтобы продолжить: ")
    if per1 == 3:
        # c()
        password = ""
        passLength = int(input("Введите длину: "))
        alph = 'ABCDEFGHIJKLANOPQRSTUVWXYZabcdefghijklanopqrstuvwxyz123456789~!@#$%^&*()-_+=|/:;"<,>.?/' #thks to rodion
        for i in range(passLength):
            password += alph[randint(0, 81)]
        print(password)
        input("\n\nНажмите Enter чтобы продолжить: ")
@d
def base64fun():#интернет
    q = int(input("1 - Зашифровать\n2 - Расшифровать\nВведите значение: "))
    if q == 2:
        # c()
        encoded_string = input("Введите строку для расшифрования: ")
        decoded_bytes = b64decode(encoded_string)
        decoded_string = decoded_bytes.decode("utf-8")
        print(decoded_string)
        input("\n\nНажмите Enter чтобы продолжить: ")
    if q == 1:
        # c()
        q = input("Введите строку для шифрования: ")
        b = q.encode("UTF-8")
        e = b64encode(b)
        s1 = e.decode("UTF-8")
        print(s1)
        input("\n\nНажмите Enter чтобы продолжить: ")
@d
def length():#я
    per3 = input("Введите строку: ")
    print("Длина строки:", len(per3))
    input("\n\nНажмите Enter чтобы продолжить: ")
@d
def ping():#я
    i1 = input(f"Введите IP, или доменное имя для пинга {'\n(или укажите параметр -t на windows, если надо пинговать бесконечно)' if clear_command == "c" else ''}: ")
    print(system(f"ping {i1}"))
    input("\n\nНажмите Enter чтобы продолжить: ")
#two
@d
def two():
    print(" 1 - PrintGPT\n 2 - Игра Камень-Ножницы-Бумага\n 3 - Игра Угадай число\n 4 - Игра Ползущие Черепашки\n 0 - Назад")
    ipt = int(input("\nВыберите действие: "))
    while ipt != 0:
        if ipt == 1:
            paintgpt()
        elif ipt == 2:
            knb()
        elif ipt == 3:
            igraUgadaika()
        elif ipt == 4:
            game_sherepash()
        elif ipt == 0:
            break
        else:
            print("Введите корректное значение")
        print(" 1 - PrintGPT\n 2 - Игра Камень-Ножницы-Бумага\n 3 - Игра Угадай число\n 4 - Игра Ползущие Черепашки\n 0 - Назад")
        ipt = int(input("\nВыберите действие: "))
@d
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
    input("\n\nНажмите Enter чтобы продолжить: ")
@d
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
    input("\n\nНажмите Enter чтобы продолжить: ")
@d
def nazad():
    done = ""
    a = -1
    print("Перевод строки в обратную сторону")
    inp = input("Введите строку: ")
    for q in inp:
        done += inp[a]
        a -= 1
    print("Ваша строка:",done)
    input("\n\nНажмите Enter чтобы продолжить: ")
@d
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
        input("\n\nНажмите Enter чтобы продолжить. ") 
@d
def paintgpt():
    spd = int(input("Введите скорость: "))
    # Задаем размер экрана 500x500 пикселей
    screensize(500, 500)
    turtle.setup(width=500, height=500)  # Окно 500x500 пикселей
    while True:
        # Задаем цвет
        colormode(255)
        color1 = (randint(0, 255), randint(0, 255), randint(0, 255))
        color2 = (randint(0, 255), randint(0, 255), randint(0, 255))
        color(color1, color2)
        # Скорость
        speed(spd)
        # Поворот
        left(randint(1, 359))
        # Генерация
        pensize(randint(4, 12))
        cur1 = randint(10, 200)
        ran1 = randint(1, 10)
        # Рандомные координаты внутри окна 500x500
        max_coord = 250  # Половина от ширины/высоты экрана
        penup()
        goto(randint(-max_coord, max_coord), randint(-max_coord, max_coord))
        pendown()
        if ran1 == 2:
            # Звезда
            begin_fill()
            for i in range(5):
                forward(150)
                left(144)
            end_fill()
        elif ran1 == 3:
            # Квадрат
            if randint(1, 2) == 1:
                begin_fill()
                for i in range(4):
                    forward(100)
                    left(90)
                end_fill()
            else:
                for i in range(4):
                    forward(100)
                    left(90)
        elif ran1 == 4:
            # Круг
            if randint(1, 2) == 1:
                begin_fill()
                circle(cur1)
                end_fill()
            else:
                circle(cur1)
        elif ran1 == 5:
            # Треугольник
            if randint(1, 2) == 1:
                begin_fill()
                for i in range(3):
                    forward(cur1)
                    left(120)
                end_fill()
            else:
                for i in range(3):
                    forward(cur1)
                    left(120)
        elif ran1 == 6:
            # Спираль
            per11 = 0
            pensize(randint(1, 10))
            for i in range(randint(10, 36)):
                forward(per11)
                per11 += 5
                left(90)
        elif ran1 == 7:
            # Пончик
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
        elif ran1 == 8:
            # Ромб
            rand = randint(50, 150)
            if randint(1, 2) == 1:
                left(randint(0, 360))
                for i in range(2):
                    left(45)
                    forward(rand)
                    left(135)
                    forward(rand)
            else:
                begin_fill()
                left(randint(0, 360))
                for i in range(2):
                    left(45)
                    forward(rand)
                    left(135)
                    forward(rand)
                end_fill()
        elif ran1 == 9:
            # Шестиугольник
            ran2 = randint(50, 150)
            if randint(1, 2) == 1:
                for i in range(6):
                    forward(ran2)
                    left(60)
            else:
                ran2 = randint(50, 150)
                begin_fill()
                for i in range(6):
                    forward(ran2)
                    left(60)
                end_fill()
        elif ran1 == 10:
            # Круговой узор
            for i in range(25):
                forward(10)
                left(25)
#linux
@d
def linux1():
    q = int(input(f"Установка разного софта{'\n*(может не работать на некоторых дистрибутивах)' if config.get('tips') else ''}\n1 - Ввести свой пакет\n2 - firefox\n3 - vlc\n4 - obs-studio\n5 - gimp\n6 - vscode\n7 - telegram-desktop*\n8 - Thunderbird\n9 - steam*\n0 - Выход \n\nВведите значение: "))
    print("\n")
    while q != 0:
        if q == 2:
            print(system("sudo install -d -m 0755 /etc/apt/keyrings && wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null && echo 'deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main' | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null && echo 'Package: *\nPin: origin packages.mozilla.org\nPin-Priority: 1000' | sudo tee /etc/apt/preferences.d/mozilla > /dev/null && sudo apt-get update && sudo apt-get install -y firefox"))
            print("\n")
            break
        elif q == 3:
            print(system("sudo apt install vlc"))
            print("\n")
            break
        elif q == 4:
            print(system("sudo apt install obs-studio"))
            print("\n")
            break
        elif q == 5:
            print(system("sudo apt install gimp"))
            print("\n")
            break
        elif q == 6:
            print(system("sudo apt-get install -y wget gpg && wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg && sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg && echo 'deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main' | sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null && rm -f packages.microsoft.gpg && sudo apt update && sudo apt install -y code"))
            print("\n")
            break
        elif q == 7:
            print(system("sudo apt install telegram-desktop"))
            print("\n")
            break
        elif q == 8:
            print(system("sudo apt install thunderbird"))
            print("\n")
            break
        elif q == 9:
            print(system("sudo apt install steam"))
            print("\n")
            break
        elif q == 1:
            c = input("Введите пакет для установки: ")
            print(system(f"sudo apt install {c}"))
            print("\n")
            break
        else:
            print("Введите корректное значение")
            print("\n")
        q = int(input(f"Установка разного софта{'\n*(может не работать на некоторых дистрибутивах)' if config.get('tips') else ''}\n1 - Ввести свой пакет\n2 - firefox\n3 - vlc\n4 - obs-studio\n5 - gimp\n6 - vscode\n7 - telegram-desktop*\n8 - Thunderbird\n9 - steam*\n0 - Выход \n\nВведите значение: "))             
@d
def linux2():
            q = int(input("apt команды\n1 - Своя команда\n2 - sudo apt update\n3 - sudo apt upgrade -y\n4 - sudo apt autoremove\n5 - update & upgrade -y\n0 - Выход \n\nВведите значение: "))
            print("\n")
            while q != 0:
                if q == 2:
                    print(system("sudo apt update"))
                    print("\n")
                elif q == 3:
                    print(system("sudo apt upgrade -y"))
                    print("\n")
                elif q == 4:
                    print(system("sudo apt autoremove"))
                    print("\n")
                elif q == 5:
                    print(system("sudo apt update && sudo apt upgrade -y"))
                    print("\n")
                elif q == 1:
                    c = input("Введите команду: ")
                    print(system(c))
                    print("\n")
                else:
                    print("Введите корректное значение.")
                    print("\n")
                q = int(input("apt команды\n1 - Своя команда\n2 - sudo apt update\n3 - sudo apt upgrade -y\n4 - sudo apt autoremove\n5 - update & upgrade -y\n0 - Выход \n\nВведите значение: "))
@d
def linux3():
            q = int(input("Системные команды\n1 - Своя команда\n2 - neofetch\n3 - uname -a\n0 - Выход \n\nВведите значение: "))
            print("\n")
            while q != 0:
                if q == 2:
                    print(system("neofetch "))
                    print("\n")
                elif q == 3:
                    print(system("uname -a"))
                    print("\n")
                elif q == 1:
                    c = input("Введите команду: ")
                    print(system(c))
                    print("\n")
                else:
                    print("Введите корректное значение.")
                    print("\n")
                q = int(input("Системные команды\n1 - Своя команда\n2 - neofetch\n3 - uname -a\n0 - Выход \n\nВведите значение: "))
                print("\n")   
@d
def linux():
    q = int(input("Линукс команды\n1 - Установка софта через apt\n2 - apt\n3 - Системные команды\n0 - Выход\n\nВведите значение: "))
    print("\n")
    while q != 0:
        if q == 1:
            linux1()
        elif q == 2:
            linux2()
        elif q == 3:
            linux3()
        else:
            print("Введите корректное значение.")
            print("\n")
        q = int(input("Линукс команды\n1 - Установка софта через apt\n2 - apt\n3 - Системные команды\n0 - Выход\n\nВведите значение: "))
        c()
@d
def todo():
    todo = []
    def printTodo():
        a = 0
        for i in todo:
            print(a + 1, "-", todo[a])
            a += 1
    printTodo()
    print("Введите номер задания чтобы отметить его как выполненое, введите N для создания нового или 0 для выхода: ")
    q =  input().lower()
    c()
    while q != "0":
        if q == "n":
            q = input("Введите задание: ")
            todo.append(q)
        else:
            del todo[int(q) - 1]
        c()
        printTodo()
        q = input("").lower()

#запуск
if config.get("setup"):
    setup()
else:
    mpy()