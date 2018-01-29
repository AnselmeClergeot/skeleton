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

def writeFile(path, template) :
     
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
        
if __name__ == '__main__' :

    init() #For colorama

    dispLogo()

    params = sys.argv[1:]

    if len(params) == 0 :
        print(Fore.RED + "Incorrect number of parameters.")
        sys.exit(-1)

    fileName = params[0]

    infos = fileInfos(fileName)

    if infos == 'forbidden' :
        print(Fore.RED + "File name is incorrect.")
        sys.exit(-1)

    elif infos == 'noextension' :
        print(Fore.RED + "Could not detect that file type.")
        createEmptyFile(fileName)
    
    else : #Our file has an extension

        name, extension = infos[0], infos[1]

        if not canWrite(fileName) : #If file already exists, don't take risk of overwriting it, quit
            print(Fore.RED + "Will not be able to create file {}, file already exists.".format(fileName))
            sys.exit(-1)


        if not templateExists(extension) : #If extension is unknown
            print(Fore.RED + "No template found for " + Style.BRIGHT + ".{}".format(extension) + Style.RESET_ALL + Fore.RED + " files.")
            createEmptyFile(fileName)

        else : #If it is a known extension

            template = 0

            if '-c' in params :
                template = choseTemplate(extension)

            writeFile(fileName, template)

    print(Fore.GREEN + "File was successfully created.")

    if not '-d' in params : #Opening
        os.system('{} {}'.format(getConfig('editor'), fileName))
