#-*- coding: utf-8 -*-

from skeleton_core import *
        
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

            writeFile(fileName, extension, template)

    print(Fore.GREEN + "File was successfully created.")

    if not '-d' in params : #Opening
        os.system('{} {}'.format(getConfig('editor'), fileName))
