#-*- coding: utf-8 -*-

import templates, files
from colorama import init, Fore, Style
import sys, os

if __name__ == '__main__' :

    init() #For colorama

    files.dispLogo()

    params = sys.argv[1:]

    if len(params) == 0 : #skeleton was called to edit templaces DB
        sys.exit(-1)

    fileName = params[0]

    infos = files.getInfos(fileName)

    if infos == 'forbidden' :
        print(Fore.RED + "File name is incorrect.")
        sys.exit(-1)

    elif infos == 'noextension' :
        print(Fore.RED + "Could not detect that file type.")
        files.createEmpty(fileName)
    
    else : #Our file has an extension

        name, extension = infos[0], infos[1]

        if not files.canWrite(fileName) : #If file already exists, don't take risk of overwriting it, quit
            print(Fore.RED + "Will not be able to create file {}, file already exists.".format(fileName))
            sys.exit(-1)


        if not templates.exists(extension) : #If extension is unknown
            print(Fore.RED + "No template found for " + Style.BRIGHT + ".{}".format(extension) + Style.RESET_ALL + Fore.RED + " files.")
            files.createEmpty(fileName)

        else : #If it is a known extension

            template = 0

            if '-c' in params :
                template = templates.askToChoose(extension)

            files.write(fileName, extension, template)

    print(Fore.GREEN + "File was successfully created.")

    if not '-d' in params : #Opening
        os.system('{} {}'.format(files.getConfig('editor'), fileName))
