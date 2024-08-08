from func import *

print(f""" 
 m    m m    m m     mmmmmmm mmmmm  mmmmm m     m
 ##  ## #    # #        #      #    #   "# "m m" 
 # ## # #    # #        #      #    #mmm#"  "#"  
 # "" # #    # #        #      #    #        #   
 #    # "mmmm" #mmmmm   #    mm#mm  #        #   {current_version} by m1cro_cat
""")
prnt_unix = " 1 - Утилиты\n 2 - Игры\n 3 - О программе\n 4 - Changelog\n 5 - Linux\n 0 - Выход"
prnt_other = " 1 - Утилиты\n 2 - Игры\n 3 - О программе\n 4 - Changelog\n 0 - Выход"
clear_command = ""
if name == "posix":
    prnt = prnt_unix
else:
    prnt = prnt_other
print(prnt)
ipt = int(input("\nВыберите действие: "))
while ipt != 0:
    if ipt == 1:
        print(" 1 - Секундомер\n 2 - Таймер\n 3 - Генератор\n 4 - Base64\n 5 - Узнать длинну строки\n 6 - Ping\n 0 - Назад")
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
            elif ipt == 0:
                break
            else:
                print("Введите корректное значение")
            print(" 1 - Секундомер\n 2 - Таймер\n 3 - Генератор\n 4 - Base64\n 5 - Узнать длинну строки\n 6 - Ping\n 0 - Назад")
            ipt = int(input("\nВыберите действие: "))
    elif ipt == 2:
        print(" 1 - Игра Камень-Ножницы-Бумага\n 2 - Игра Угадай число\n 0 - Назад")
        ipt = int(input("\nВыберите действие: "))
        while ipt != 0:
            if ipt == 1:
                knb()
            elif ipt == 2:
                igraUgadaika()
            elif ipt == 0:
                break
            else:
                print("Введите корректное значение")
            print(" 1 - Игра Камень-Ножницы-Бумага\n 2 - Игра Угадай числоn 0 - Назад")
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
