#-*- coding: utf-8 -*-

from colorama import init, Fore, Back, Style
import sys, os

init()

def getPath(fileName) :
    return os.path.join(sys.path[0], fileName)

def sayHello() :
    with open(getPath('logo'), 'r') as logo_file :
        logo = logo_file.read()

        print(Style.BRIGHT + Fore.CYAN + logo)
        print(Fore.GREEN + "Simple file skeleton generator 1.0.0\n")

def askFile() :
    fullName = raw_input(Style.RESET_ALL + Style.BRIGHT + Fore.BLUE + "Enter the name of your file with extension : " + Style.RESET_ALL)

    if len(fullName) == 0 :
        print(Style.BRIGHT + Fore.RED + "You entered nothing.")
        return -1

    parsed = fullName.split('.')

    if len(parsed) == 1 :
        print(Style.BRIGHT + Fore.RED + "Your file has no extension.")
        return -1

    name, extension = parsed[0], parsed[1]

    if len(name) == 0 :
        print(Style.BRIGHT + Fore.RED + "Your file has no name.")
        return -1
        
    if len(extension) == 0 :
        print(Style.BRIGHT + Fore.RED + "Your file hs no extension.")
        return -1

    return name, extension

def getFileType(fileName) :

    return fileName[fileName.index('.')+1:]

def writeFile(fileName, content) :
    try :
        newFile = open(os.path.join(os.getcwd(), fileName), 'w')
        newFile.write(content)
    except :
        print(Style.BRIGHT + Fore.RED + "Cannot create file. Try running skeleton with sudo or check filename.")
        return

    print(Style.BRIGHT + Fore.GREEN + "File created.")

def chooseTemplate(fileType) :
    path = getPath(os.path.join('templates', fileType))

    if not os.path.exists(path) :
        print(Style.BRIGHT + Fore.RED + "No templates were found for .{} files.".format(fileType))

    else :
        templatesNb = len([f for f in os.listdir(path)])
        print(Style.BRIGHT + Fore.GREEN + "{} template(s) existing for .{} files.".format(templatesNb, fileType))
    
if __name__ == '__main__' :

    sayHello()
    results = askFile()

    if results != -1 :
