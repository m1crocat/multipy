from func import *
print(f""" 
 m    m m    m m     mmmmmmm mmmmm  mmmmm m     m
 ##  ## #    # #        #      #    #   "# "m m" 
 # ## # #    # #        #      #    #mmm#"  "#"  
 # "" # #    # #        #      #    #        #   
 #    # "mmmm" #mmmmm   #    mm#mm  #        #   {current_version} by m1cro_cat
""")
prnt_unix = " 1 - Утилиты\n 2 - Игры\n 3 - О программе\n 4 - Changelog\n 5 - Linux\n \n 0 - Выход"
prnt_other = " 1 - Утилиты\n 2 - Игры\n 3 - О программе\n 4 - Changelog\n 0 - Выход"
clear_command = ""
if os.name == "posix":
    prnt = prnt_unix
    clear_command = "clear"
else:
    prnt = prnt_other
    clear_command = "clr"
print(prnt)
ipt = int(input("\nВыберите действие: "))
while ipt != 0:
    if ipt == 1:
        print(" 1 - Секундомер\n 2 - Таймер\n 3 - Генератор\n 4 - Base64\n 5 - Узнать длинну строки\n 6 - Ping\n 7 - Конвертор единиц (beta)\n 0 - Назад")
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
                convertor()
            elif ipt == 0:
                break
            else:
                print("Введите корректное значение")
            print(" 1 - Секундомер\n 2 - Таймер\n 3 - Генератор\n 4 - Base64\n 5 - Узнать длинну строки\n 6 - Ping\n 7 - Конвертор единиц (beta)\n 0 - Назад")
            ipt = int(input("\nВыберите действие: "))
    elif ipt == 2:
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
    elif ipt == 3:
        info()
    elif ipt == 4:
        changelog()
    elif ipt == 5:
        linux()
    elif ipt == 0:
        break
    else:
        print("Введите корректное значение")
    print(prnt)
    ipt = int(input("\nВыберите действие: "))
print("exit...")
sleep(1)
