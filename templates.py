#-*- coding: utf-8 -*-

import os, sys
from colorama import init, Fore, Style
from paths import *

def exists(extension) :
    templatePath = getTemplatePath(extension)
    return os.path.exists(templatePath) and len(os.listdir(templatePath)) > 0

def displayList(extension) :
    
    templatePath = getTemplatePath(extension)
    templateNum = len(os.listdir(templatePath))

    for i in range(templateNum) :
        with open(os.path.join(templatePath, str(i))) as template :
            desc = template.readline().strip()
            print(Fore.CYAN + "{}) ".format(i) + desc)

    return templateNum

def askToChoose(extension) :

    templateNum = displayList(extension)
    choiceCorrect = False

    while not choiceCorrect :
        choiceCorrect = True

        try :
            choice = int(raw_input(Fore.CYAN + "Chose : "))

            if not (0 <= choice < templateNum) :
                print(Fore.RED + "Please chose an existing template.")
                choiceCorrect = False

        except ValueError :
            print(Fore.RED + "Please unter a number.")
            choiceCorrect = False

    return choice
