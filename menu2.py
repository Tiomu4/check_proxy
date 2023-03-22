import numpy as np
from actions import *
from all_menus import *
import sys

def mainMenu():
    while True:
        displayMenu(mainMenu_1)
        choice = choose_choice(mainMenu_1)
        if mainMenu_1[choice] == "Proxy":
            choose_action_by_choice_1(proxyMenu_2,choice)
        elif mainMenu_1[choice] == "Relax":
             choose_action_by_choice_1(relaxMenu_2,choice)
        elif mainMenu_1[choice] == "Study":
             choose_action_by_choice_1(studyMenu_2,choice)
        elif mainMenu_1[choice] == "Finance":
            choose_action_by_choice_1(financeMenu_2,choice)

        elif choice == 0:
            sys.exit()


mainMenu()
