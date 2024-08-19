from func import *
@decor
def mpy():
    print(f""" 
 m    m m    m m     mmmmmmm mmmmm  mmmmm m     m
 ##  ## #    # #        #      #    #   "# "m m" 
 # ## # #    # #        #      #    #mmm#"  "#"  
 # "" # #    # #        #      #    #        #   
 #    # "mmmm" #mmmmm   #    mm#mm  #        #   {current_version} by m1cro_cat
""")
    print(prnt)
    ipt = int(input("\nВыберите действие: "))
    while ipt != 0:
        if ipt == 1:
            clr(clear_command)
            print(" 1 - Секундомер\n 2 - Таймер\n 3 - Генератор\n 4 - Base64\n 5 - Узнать длинну строки\n 6 - Ping\n 7 - Конвертор единиц (beta)\n 8 - Перевод строки наоборот\n 0 - Назад")
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
                elif ipt == 8:
                    nazad()
                elif ipt == 0:
                    break
                else:
                    print("Введите корректное значение")
                print(" 1 - Секундомер\n 2 - Таймер\n 3 - Генератор\n 4 - Base64\n 5 - Узнать длинну строки\n 6 - Ping\n 7 - Конвертор единиц (beta)\n 8 - Перевод строки наоборот\n 0 - Назад")
                ipt = int(input("\nВыберите действие: "))
        elif ipt == 2:
            clr(clear_command)
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
            clr(clear_command)
            info()
        elif ipt == 4:
            clr(clear_command)
            changelog()
        elif ipt == 5 and clear_command == "clr":
            clr(clear_command)
            linux()
        elif ipt == 5 and clear_command == "clear":
            clr(clear_command)
            settings()
        elif ipt == 6:
            clr(clear_command)
            settings()
        elif ipt == 0:
            break
        else:
            print("Введите корректное значение")
        print(prnt)
        ipt = int(input("\nВыберите действие: "))
mpy()

