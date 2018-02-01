#-*- coding: utf-8 -*-

import os, sys
from colorama import init, Fore, Style
from paths import *

def dispLogo() :
    with open(getLogoPath(), 'r') as logo_file :
        print(Style.BRIGHT + Fore.CYAN + logo_file.read() + Style.RESET_ALL)

def getInfos(fileName) :
    base = os.path.splitext(os.path.basename(fileName))
    name, extension = base[0], base[1][1:]

    if len(name) != 0 and len(extension) != 0 :
        return base, extension

    elif name == '.' :
        return 'forbidden'

    else :
        return 'noextension'

def canWrite(path) :
    return not os.path.exists(path)

def write(path, extension, template) :
     
    templatePath = getTemplatePath(extension)

    with open(os.path.join(templatePath, str(template)), 'r') as template :
        content = '\n'.join(template.read().split('\n')[1:])
        
        with open(path, 'w') as newFile :
            newFile.write(content)

def createEmpty(path) :
    with open(path, 'w') as newFile :
        pass

def getConfig(param) :

    with open(getCfgPath(), 'r') as cfg_file :
        content = cfg_file.read().split('\n')

        for line in content :
            parsedLine = line.strip().split('=')
            if parsedLine[0].replace(' ', '')  == param :
                return parsedLine[1].replace(' ', '')
