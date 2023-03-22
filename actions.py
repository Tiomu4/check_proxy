import webbrowser
import os
import subprocess
import sys
import selenium_main
import check_iproxy

from all_menus import *


def displayMenu(menuItems):
    numeration = 1
    for i in menuItems[1:]:
        print("[", numeration, "]", i)
        numeration += 1


def choose_choice(menu):
    choice = -1
    while choice < 0 or choice == "":
        choice = int(input(">>>> "))
    return choice


def is_digit_in_number(digit, number):
    return str(digit) in str(number)


def choose_action_by_choice_1(menu, choice):


    if menu[0] == "proxyMenu_2":
        while choice != 0:
            displayMenu(proxyMenu_2)
            choice = choose_choice(menu)
            if is_digit_in_number("1", choice) == True:
                webbrowser.open("https://iproxy.online/app/", autoraise=True)
                """ subprocess.check_output(['open','http://google.com/','--hide']) """
            if is_digit_in_number("2", choice) == True:
                webbrowser.open("https://www.olx.pl/obserwowane/wyszukiwania/")
                webbrowser.open("https://allegro.pl/moje-allegro/zakupy/obserwowane/wyszukiwania")
            if is_digit_in_number("3", choice) == True:
                """ webbrowser.open("https://nowymoj.t-mobile.pl/")
                webbrowser.open("https://web.telegram.org/z/#1910466769") """
                check_iproxy.rent_date()
                selenium_main.t_mobile_script()
            if is_digit_in_number(0, choice) == True:
                sys.exit()
            if is_digit_in_number(8, choice) == True:
                break

    if menu[0] == "financeMenu_2":
        while choice != 0:
            displayMenu(financeMenu_2)
            choice = choose_choice(menu)
            if is_digit_in_number(1, choice) == True:
                webbrowser.open(
                    "https://www.binance.com/en/my/wallet/account/overview")
            if is_digit_in_number(2, choice) == True:
                webbrowser.open(
                    "https://www.binance.com/en/my/wallet/account/payment/dashboard")
            if is_digit_in_number(3, choice) == True:
                webbrowser.open(
                    "https://p2p.binance.com/en/trade/BankPekao/USDT?fiat=PLN")
            if is_digit_in_number(4, choice) == True:
                webbrowser.open(
                    "https://next.privat24.ua/exchange-rates")    
            if is_digit_in_number(8, choice) == True:
                break
            if is_digit_in_number(0, choice) == True:
                sys.exit()

    if menu[0] == "relaxMenu_2":
        while choice != 0:
            displayMenu(relaxMenu_2)
            choice = choose_choice(menu)
            if is_digit_in_number(1, choice) == True:
                webbrowser.open("brave://history/?q=animego")
            if is_digit_in_number(2, choice) == True:
                 webbrowser.open("https://youtube.com")
            if is_digit_in_number(3, choice) == True:
                 choose_action_by_choice_1(gameMenu_3, choice)
            elif is_digit_in_number(8, choice) == True:
                break
            if is_digit_in_number(0,choice) == True:
                sys.exit()
    
    if menu[0] == "studyMenu_2":
        while choice != 0:
            displayMenu(studyMenu_2)
            choice = choose_choice(menu)
            if is_digit_in_number(1, choice) == True:
                os.startfile("D:\Pollub\Java")
            if is_digit_in_number(2, choice) == True:
                choose_action_by_choice_1(AnalizaMenu_3, choice)
            if is_digit_in_number(3, choice) == True:
                os.startfile("D:\Pollub\Baza")
            if is_digit_in_number(4, choice) == True:
                choose_action_by_choice_1(matematykaMenu_3, choice)
            if is_digit_in_number(5, choice) == True:
                os.startfile("D:\Pollub\Elektrotechnika")
            if is_digit_in_number(6, choice) == True:
                os.startfile("D:\Pollub\Metrologia")
            elif is_digit_in_number(8, choice) == True:
                break

            if is_digit_in_number(0,choice) == True:
                sys.exit()

    if menu[0] == "gameMenu_3":
        while choice != 0:
            displayMenu(gameMenu_3)
            choice = choose_choice(menu)
            if is_digit_in_number(1, choice) == True:
                os.startfile(r"C:\Users\Artem\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Wargaming.net\World_of_Tanks_EU\World of Tanks EU")
            if is_digit_in_number(2, choice) == True:
                os.startfile(r"D:\SteamLibrary\steamapps\common\Counter-Strike Global Offensive\csgo.exe")
            elif is_digit_in_number(8, choice) == True:
                break
            if is_digit_in_number(0,choice) == True:
                sys.exit()


    if menu[0] == "AnalizaMenu_3":
        while choice != 0:
            displayMenu(AnalizaMenu_3)
            choice = choose_choice(menu)
            if is_digit_in_number(1, choice) == True:
                os.startfile("D:\Pollub\Analiza")
            if is_digit_in_number(2, choice) == True:
                webbrowser.open("https://moodle3.cs.pollub.pl/course/view.php?id=1209")
                webbrowser.open("https://moodle3.cs.pollub.pl/course/view.php?id=1178")
            elif is_digit_in_number(8, choice) == True:
                break
            if is_digit_in_number(0,choice) == True:
                sys.exit()

    if menu[0] == "matematykaMenu_3":
        while choice!= 0:
            displayMenu(matematykaMenu_3)
            choice = choose_choice(menu)
            if is_digit_in_number(1, choice) == True:
                os.startfile("D:\Pollub\Matematyka")
            if is_digit_in_number(2, choice) == True:
                webbrowser.open("https://moodle3.cs.pollub.pl/course/view.php?id=262")
            if is_digit_in_number(3, choice) == True:
                os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneNote.lnk")

    