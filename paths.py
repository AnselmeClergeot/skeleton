#-*- coding: utf-8 -*-

import os, sys

scriptDir = os.path.dirname(os.path.realpath(__file__))

def getTemplatePath(extension) :
    return os.path.join(scriptDir, 'templates', extension)

def getLogoPath() :
    return os.path.join(scriptDir, 'logo')

def getCfgPath() :
    return os.path.join(scriptDir, 'cfg')
