current_version = "3.1.7"
release_type = "stable"
version_date = "18.01.24"
config_file = 'config.json'

from random import *
from time import *
from turtle import *
import os
import sys
import base64
import requests
import shutil
import main_beta
import json
import traceback

def amogus():#инет
            speed(15)
            color1 = (randint(0, 255), randint(0, 255), randint(0, 255))
            color2 = (randint(0, 255), randint(0, 255), randint(0, 255))
            pensize(30)
            fillcolor(color1)
            begin_fill()
            right(90)
            forward(50)
            right(180)
            circle(40, -180)
            right(180)
            forward(200)
            right(180)
            circle(100, -180)
            backward(20)
            left(15)
            circle(500, -20)
            backward(20)
            circle(40, -180)
            left(7)
            backward(50)
            up()
            left(90)
            forward(10)
            right(90)
            down()
            right(240)
            circle(50, -70)
            end_fill()
            up()
            right(230)
            forward(100)
            left(90)
            forward(20)
            right(90)
            down()
            fillcolor(color2)
            begin_fill()
            right(150)
            circle(90, -55)
            right(180)
            forward(1)
            right(180)
            circle(10, -65)
            right(180)
            forward(110)
            right(180)
            circle(50, -190)
            right(170)
            forward(80)
            right(180)
            circle(45, -30)
            end_fill()
            up()
            right(60)
            forward(100)
            right(90)
            forward(75)
            fillcolor(color2)
            begin_fill()
            down()
            forward(30)
            right(255)
            circle(300, -30)
            right(260)
            forward(30)
            end_fill()
def toggleUpdates():#MystieHum\нейросеть

    if os.path.exists(config_file):
        with open(config_file) as f:
            config = json.load(f)
    else:
        config = {
            'updates_enabled': True
        }

    if config['updates_enabled'] == True:
        update_state = "включена"
    elif config['updates_enabled'] == False:
        update_state = "выключена"
    choice = input(f"1 / 0 - вкл/выкл автоматическую проверку обновлений\nСейчас автопроверка обновлений {update_state}.\nВыберите опцию: ")
    
    if choice == '1':
        print("Обновления включены")
        config['updates_enabled'] = True
    elif choice == '0':
        print("Обновления отключены")
        config['updates_enabled'] = False

    with open(config_file, 'w') as f:
        json.dump(config, f)

if __name__ == '__main__':#MystieHum\нейросеть
    
    toggleUpdates()
    
    # Check config setting
    if os.path.exists(config_file):
        with open(config_file) as f:
            config = json.load(f)
            if config['updates_enabled']:
                print("Обновления включены")
                # call update code
            else:
                print("Обновления отключены")
    else:
        print("Обновления включены по умолчанию")

def miscMenu():#MystieHum\нейросеть
	try:
		while True:
			choice = int(input("\n1 - проверить обновления\n2 - настроить проверку обновлений\n3 - переключить ветку обновлений\n4 - скачать последную версию\n5 - выйти в главное меню\nВыберите опцию: "))
			if choice == 1:
				checkForUpdates()
			elif choice == 2:
				toggleUpdates()
			elif choice == 3:
				switchBranch()
			elif choice == 4:
				dlLastVer()
			elif choice == 5:
				break
			else:
				print("Такой опции не существует")
	except ValueError:
		print("Неправильное значение! Должно быть от 1 до 5!")

def dlLastVer():#MystieHum\нейросеть
	if os.path.exists(config_file):
		with open(config_file) as f:
			config = json.load(f)
	branch = config['update_branch']
	version_url = f'https://raw.githubusercontent.com/m1crocat/multipy/{branch}/latest_version.txt'
	version_response = requests.get(version_url)

	if version_response.status_code == 200:
		latest_version = version_response.text.strip()
		zip_url = f'https://github.com/m1crocat/multipy/archive/{branch}.zip'
		save_file = f'mpy-{latest_version}-{branch}.zip'
		save_path = os.path.join(os.getcwd(), save_file)

		response = requests.get(zip_url)
		with open(save_path, 'wb') as f:
			f.write(response.content)

		print(f"Новая версия сохранена по пути:\n{save_path}")
		return save_path

	else:
		print("Произошла ошибка при скачивании. Простите позязя :(")
		return None

def prt():#я
    print(" <<MultiPy>> \n 1 - PaintGPT \n 2 - О MultiPy \n 3 - Что нового? \n 4 - Игра КНБ \n 5 - Игра Угадай число \n 6 - Секундомер \n 7 - Таймер обратного отсчета \n 8 - Разное \n 9 - Бросить кубик \n 10 - Погода \n 11 - Генератор \n 12 - Base64 \n 13 - Узнать длину строки (len) \n 14 - Beta \n 15 - Ping \n 16 - Обновления \n 17 - Конвертор(alpha)")
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

def updateProgram():#MystieHum\нейросеть
	if os.path.exists(config_file):
		with open(config_file) as f:
			config = json.load(f)
	branch = config['update_branch']
	url = f'https://github.com/m1crocat/multipy/archive/{branch}.zip'
	update_zip = os.path.join('cache', 'update.zip')
	os.makedirs('cache', exist_ok=True)
	response = requests.get(url)
	with open(update_zip, 'wb') as f:
		f.write(response.content)
	shutil.unpack_archive(update_zip, 'update')
	os.remove(update_zip)
	src_dir = os.path.join('update', f'multipy-{branch}')
	dest_dir = os.path.dirname(os.path.abspath(__file__))
	for src_name in os.listdir(src_dir):
		src_path = os.path.join(src_dir, src_name)
		dest_path = os.path.join(dest_dir, src_name)
		if os.path.exists(dest_path):
			os.remove(dest_path)
		shutil.move(src_path, dest_dir)
	shutil.rmtree(os.path.join('update'))
	shutil.rmtree(os.path.join('cache'))
	print("Обновление завершено успешно!\n")
	args = [sys.executable] + sys.argv
	os.execv(sys.executable, args)

def checkForUpdates():#MystieHum\нейросеть
	if os.path.exists(config_file):
		with open(config_file) as f:
			config = json.load(f)
	branch = config['update_branch']
	print("Проверка обновлений.. ")
	cache_dir = os.path.join('cache')
	if os.path.isdir(cache_dir):
		shutil.rmtree(cache_dir)
	cache_folder = 'cache'
	if not os.path.exists(cache_folder):
		os.mkdir(cache_folder)
	latest_version_url = f'https://raw.githubusercontent.com/m1crocat/multipy/{branch}/latest_version.txt'
	latest_version_path = os.path.join(cache_folder, 'latest_version.txt')
	if not os.path.exists(latest_version_path):
		response = requests.get(latest_version_url)
		with open(latest_version_path, 'w') as f:
			f.write(response.text)
	with open(latest_version_path) as f:
		latest_version = f.read().strip()
	if latest_version > current_version:
		print(f"Доступна новая версия {latest_version} (текущая версия: {current_version})")
		update = input("Хотите обновиться? (y/n): ")
		if update.lower() == 'y' or update.lower() == 'д':
			print("Обновляемся...")
			updateProgram()
		elif update.lower() == 'n' or update.lower() == 'н':
			sleep(0.3)
			print("Обновление отменено\n")
			shutil.rmtree(os.path.join('cache'))
	else:
		print("Обновлений не найдено!\n")
		shutil.rmtree(os.path.join('cache'))

def switchBranch():#MystieHum\нейросеть
	while True:
		if os.path.exists(config_file):
			with open(config_file) as f:
				config = json.load(f)
		print(f"Сейчас используется ветка {config['update_branch']} для обновлений.\n")
		print("1 - переключиться на beta")
		print("2 - переключиться на main")
		print("3 - в главное меню")
		choice = input("Выберите опцию: ")
		if choice == '1':
			config['update_branch'] = "beta"
			with open(config_file, 'w') as f:
				json.dump(config, f)
		elif choice == '2':
			config['update_branch'] = "main"
			with open(config_file, 'w') as f:
				json.dump(config, f)
		elif choice == '3':
			break
		print(f"Вы переключились на ветку {config['update_branch']}.")

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
            if ran1 == 1:
                 amogus()
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
    print(f"\nПрограмма MultiPy.\nВерсия {current_version} {release_type} от {version_date}.")

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

def raznoe():#я
    ipt1 = int(input("1 - Интересный узор\n2 - AMOGUS\n3 - Бенчмарк\nВыберите что-нибудь: "))
    if ipt1 == 1:
        try:
            hideturtle()
            per2 = 10
            per1 = 1
            while True:
                speed(per2)
                forward(per1)
                left(90)
                per1 += 1
                per2 += 1
        except Exception:
            print("Закрыто")
    elif ipt1 == 2:
        amogus()
    elif ipt1 == 3:
         bench()
    else:
        print("дУ ю СпИк ИнГлИш?!!?")
def bench():#я(идея моя)
     input("Для начала теста нажмите Enter: ")
     time_st = time()
     sleep(5)
     time_end = time()
     print("Результат теста:", (time_end - time_st) - 5, "сек. время вычислений")
def weather():# нейросеть
    print("Команда полностью написана через ChatGPT")
    city = input("Введите название города: ")
    api_key = '9f847b92b31f51a681d9792e18973c03'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    if weather_data['cod'] == 200:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"Температура в городе {str(city).capitalize()}: {temperature}°C, {description}")
    else:
        print("Не удалось получить данные о погоде") 

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
    i1 = input("Введите ip, или доменное имя для пинга (укажите после ip -t если надо пинговать бесконечно): ")
    print(os.system(f"ping {i1}"))

def changelog():#я
    print("\nЛист обновлений!\n")
    print("3.1.7 - 18.01.24")
    print("Мини-обнова. MystieHum больше не разработчик программы. ")
    print("3.1.6 - 09.11.23")
    print("Обновление, аМоГуС в PaintGPT")
    print("3.1.5.9 - 09.11.23")
    print("Починил то что сломал(кошк)")
    print("3.1.5.8 - 07.11.23")
    print("Если при проверке обновлений произойдет ошибка, то программа продолжит работу (m1cro_cat)")
    print("3.1.5.7 - 03.11.23")
    print("Имя файлов скачанных версий теперь mpy-{версия}-{ветка}.zip (MystieHum)")
    print("3.1.5.6 - 03.11.23")
    print("Переименован пункт 'настроить обновления' в 'настроить проверку обновлений', чтобы избежать путаницы.\nТакже немного прибран код (MystieHum)")
    print("3.1.5.5 - 03.11.23")
    print("Фикс перевода, фикс даты. (кот)")
    print("3.1.5.3-4 - 03.11.23")
    print("Возможность скачать последнюю версию через п.16 (Обновления) (MystieHum & m1cro_cat)")
    print("3.1.5-3.1.5.2 - 02.11.23")
    print("Переключение ветки обновлений (MystieHum (он молодец))")
    print("3.1.4.8 - 02.11.23")
    print("Важный фикс обновлений (m1cro_cat)")
    print("3.1.4.6 - 26.08.23")
    print("Фиск игры Угадай число")
    print("3.1.4.2-5 - 22-25.08.23")
    print("Фиксы")
    print("3.1.4.1 - 22.08.23")
    print("хот дог фиксы(у байтов отвал(хнык хнык))")
    print("3.1.4 - 22.08.23")
    print("Добавление конвертора(п. 17), минификсы")
    print("3.1.3.1 - 22.08.23")
    print("Поздравляю свою маму с днем рождения, эта версия для тебя :3")
    print("3.1.3 - 20.08.23")
    print("Добавлена настройка автопроверки обновлений (п. 16)\n")
    print("3.1.1 / 3.1.2 - 20.08.23")
    print("Перенос всех функций в отдельный файл, крч внутренняя переделка:)\n")
    print("3.1.0 - 20.08.23")
    print("Проверка и установка обновлений\nПеределанный таймер и секундомер\nМелкие исправления\n")
    print("3.0.4 - 18.08.23")
    print("Фиксы, улучшение кода PaintGPT\n")
    print("3.0.3 - 17.08.23")
    print("Много разных фиксов от MystieHum\n")
    print("3.0.1 / 3.0.2 - 15-16.08.23")
    print("Минификсы, улучшение PaintGPT, других команд.\n")
    print("3.0.0 - 11.08.23")
    print("Полностью переписан интерфейс, улучшен код)\n")
    print("2.2.1 - 11.08.23")
    print("Финальная версия 2.x\n")
    print("2.2.0 - 11.08.23")
    print("Переименование программы \nОптимизация кода\n")
    print("2.1.0 - 09.08.23")
    print("Переделка некоторых функций, и добавление новых\n")
    print("2.0.0 - 28.07.23")
    print("Полная переделка кода, убрал лишние функции, которые уже не актуальны. Также добавил кучу всего!\n")
    print("1.5.0 - 16.07.23")
    print("Переименовал в projectpb \nДобавил много функций\n")


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
