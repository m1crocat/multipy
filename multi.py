from func import *
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
        elif ipt == 5 and clear_command == "clear":
            linux()
        elif ipt == 5 and clear_command == "clr":
            settings()
        elif ipt == 6:
            settings()
        elif ipt == 123:
            reboot()
        elif ipt == 0:
            break
        else:
            print("Введите корректное значение")
        print(prnt)
        ipt = int(input("\nВыберите значение: "))
config = open_config()
if config.get("setup"):
    setup()
else:
    mpy()