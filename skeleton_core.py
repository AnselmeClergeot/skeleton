#-*- coding: utf-8 -*-

import os, sys
from colorama import init, Fore, Style
from paths import *

def dispLogo() :
    with open(getLogoPath(), 'r') as logo_file :
        print(Style.BRIGHT + Fore.CYAN + logo_file.read() + Style.RESET_ALL)

def fileInfos(fileName) :
    base = os.path.splitext(os.path.basename(fileName))
    name, extension = base[0], base[1][1:]

    if len(name) != 0 and len(extension) != 0 :
        return base, extension

    elif name == '.' :
        return 'forbidden'

    else :
        return 'noextension'

def templateExists(extension) :
    templatePath = getTemplatePath(extension)
    return os.path.exists(templatePath) and len(os.listdir(templatePath)) > 0

def displayTemplates(extension) :
    
    templatePath = getTemplatePath(extension)
    templateNum = len(os.listdir(templatePath))

    for i in range(templateNum) :
        with open(os.path.join(templatePath, str(i))) as template :
            desc = template.readline().strip()
            print(Fore.CYAN + "{}) ".format(i) + desc)

    return templateNum

def choseTemplate(extension) :

    templateNum = displayTemplates(extension)
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

def canWrite(path) :
    return not os.path.exists(path)

def writeFile(path, extension, template) :
     
    templatePath = getTemplatePath(extension)

    with open(os.path.join(templatePath, str(template)), 'r') as template :
        content = '\n'.join(template.read().split('\n')[1:])
        
        with open(path, 'w') as newFile :
            newFile.write(content)

def createEmptyFile(path) :
    with open(path, 'w') as newFile :
        pass

def getConfig(param) :

    with open(getCfgPath(), 'r') as cfg_file :
        content = cfg_file.read().split('\n')

        for line in content :
            parsedLine = line.strip().split('=')
            if parsedLine[0].replace(' ', '')  == param :
                return parsedLine[1].replace(' ', '')
