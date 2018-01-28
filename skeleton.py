#-*- coding: utf-8 -*-

import os, sys
from colorama import init, Fore, Style

def dispLogo() :
    logoPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logo')
    with open(logoPath, 'r') as logo_file :
        print(Style.BRIGHT + Fore.CYAN + logo_file.read() + Style.RESET_ALL)

def fileInfos(fileName) :
    base = os.path.splitext(os.path.basename(fileName))
    name, extension = base[0], base[1][1:]
    
    if len(name) != 0 and len(extension) != 0 :
        return base, extension

    else :
        return -1

def templateExists(extension) :
    templatesPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates', extension)

    return os.path.exists(templatesPath) and len(os.listdir(templatesPath)) > 0

def displayTemplates(extension) :
    
    templatesPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates', extension)

    templateNum = len(os.listdir(templatesPath))

    for i in range(templateNum) :
        with open(os.path.join(templatesPath, str(i))) as template :
            desc = template.readline().strip()
            print(Fore.CYAN + "{}) ".format(i) + desc)

    print('')
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
     
    templatesPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates', extension)

    with open(os.path.join(templatesPath, str(template)), 'r') as template :
        content = '\n'.join(template.read().split('\n')[1:])
        
        with open(path, 'w') as newFile :
            newFile.write(content)
        
if __name__ == '__main__' :

    dispLogo()

    init() #For colorama

    params = sys.argv[1:]

    if len(params) == 0 :
        print(Fore.RED + "Error, incorrect number of parameters.")
        sys.exit(-1)

    fileName = params[0]

    results = fileInfos(fileName)

    if results == -1 :
        print(Fore.RED + "Error, incorrect file name.")
        sys.exit(-1)

    name, extension = results[0], results[1]

    if not canWrite(fileName) :
        print(Fore.RED + "Will not be able to create file {}, file already exists.".format(fileName))
        sys.exit(-1)


    if not templateExists(extension) :
        print(Fore.RED + "No template found for " + Style.BRIGHT + ".{}".format(extension) + Style.RESET_ALL + Fore.RED + " files.")
        sys.exit(-1)


    template = 0

    if '-t' in params :
        template = choseTemplate(extension)

    writeFile(fileName, template)
    print(Fore.GREEN + "File was successfully created.")

