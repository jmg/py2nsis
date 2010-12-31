# -*- coding: utf-8 -*- 

import os
import shutil

from Lib.Constants import *

class AppData(object):

    def __init__(self, frame):

        self.version = frame.tbVersion.GetValue()
        self.company_name = frame.tbCompany.GetValue()
        self.copyright = frame.tbCopyright.GetValue()
        self.name = frame.tbAppName.GetValue()
        
        self.includes = []
        for i in range(frame.lbModules.GetCount()):
            self.includes.append(frame.lbModules.GetString(i).decode('ascii'))
        
        self.packages = []
        
        self.excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
                                'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
                                'Tkconstants', 'Tkinter']
                                                
        self.main_script = frame.fpMainScript.GetPath()
        if self.main_script.find("\\\\") == -1:
            self.main_script = self.main_script.replace("\\","\\\\")
        
        self.main = self.main_script[:-3].split("\\")[-1]
        self.root = self.main_script[:self.main_script.rindex("\\")]
        
        dist = frame.tbDist.GetValue()
        if dist == '':
            self.dist = self.root + "\\" + DEFAULT_DIST
        else:
            self.dist = self.root + "\\" + dist
        
        self.data_files = []
        for i in range(frame.lbDirs.GetCount()):
            path = frame.lbDirs.GetString(i)
            if path.find("\\\\") == -1:
                path = path.replace("\\","\\\\")
            dir = path[path.rindex(self.root)+len(self.root):path.rindex("\\")]
            self.data_files.append((self.dist + dir , [path]))
            
        self.nsisPath = frame.nsisPath
        
        self.logo = frame.fpLogo.GetPath()
        if self.logo.find("\\\\") == -1:
            self.logo = self.logo.replace("\\","\\\\")
        
        if os.path.exists(self.dist):
            shutil.rmtree(self.dist)
            
        if hasattr(frame, 'custom_code'):
            self.custom_code = frame.custom_code
        else:
            self.custom_code = ""
            
        self.bundle = frame.cbBundle.GetValue()
        self.setup = frame.ckSetup.GetValue()
