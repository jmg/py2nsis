# -*- coding: utf-8 -*-

import os
import shutil

from Lib.Constants import *

class AppData(object):
    """ Class to generate the data object wich contains the parameters
        to generate both, the setup.py and the installer.nsi
        This class must be serializable in order to save the file projects
        and allow users to reload its.

        params:
            - frame: the FrmApplication from main.py
        returns:
            - a data object for setup.py and installer.nsi
    """

    def __init__(self, frame):

        #general atributes of the project
        self.version = frame.tbVersion.GetValue()
        self.company_name = frame.tbCompany.GetValue()
        self.copyright = frame.tbCopyright.GetValue()
        self.name = frame.tbAppName.GetValue()

        #additional python modules list
        self.includes = []
        for i in range(frame.lbModules.GetCount()):
            self.includes.append(frame.lbModules.GetString(i).encode('ascii'))

        #Todo: impliment packages
        self.packages = []

        #Excludes are legacy from GUI2Exe
        self.excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
                                'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
                                'Tkconstants', 'Tkinter']

        #main script file
        self.main_script = frame.fpMainScript.GetPath()
        #replace '\' to space this character
        if self.main_script.find("\\\\") == -1:
            self.main_script = self.main_script.replace("\\","\\\\")

        #the name of the main script without .py
        self.main = self.main_script[:-3].split("\\")[-1]
        #the root dir of the project
        self.root = self.main_script[:self.main_script.rindex("\\")]

        #the dir in where the py2exe generate the files
        dist = frame.tbDist.GetValue()
        if dist == '':
            self.dist = self.root + "\\" + DEFAULT_DIST
        else:
            self.dist = self.root + "\\" + dist

        #generate a list of tuples of data files for py2exe
        self.data_files = []
        for i in range(frame.lbDirs.GetCount()):
            path = frame.lbDirs.GetString(i)
            if path.find("\\\\") == -1:
                path = path.replace("\\","\\\\")
            dir = path[path.rindex(self.root)+len(self.root):path.rindex("\\")]
            self.data_files.append((self.dist + dir , [path]))

        #generate a list of tuples (Table Of Contents) for pyInstaller
        #FIXME: extract to a method, this sucks!
        self.datas = []
        for i in range(frame.lbDirs.GetCount()):
            path = frame.lbDirs.GetString(i)
            if path.find("\\\\") == -1:
                path = path.replace("\\","\\\\")
            dir = path[path.rindex(self.root)+len(self.root)+len("\\"):]
            self.datas.append((dir.encode('ascii'), path.encode('ascii') ,'DATA'))

        #the path to nsis install dir
        self.nsisPath = frame.nsisPath

        #the logo for the exe and installer
        self.logo = frame.fpLogo.GetPath()
        if self.logo.find("\\\\") == -1:
            self.logo = self.logo.replace("\\","\\\\")

        #remove the old dist dir if exists
        if os.path.exists(self.dist):
            shutil.rmtree(self.dist)

        #the custom python code
        if hasattr(frame, 'custom_code'):
            self.custom_code = frame.custom_code
        else:
            self.custom_code = ""

        self.bundle = frame.cbBundle.GetValue()
        self.setup = frame.ckSetup.GetValue()
