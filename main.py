# -*- coding: utf-8 -*- 
import wx
import os
import subprocess
import pickle
import ConfigParser
import shutil

from distutils.core import setup
import warnings 
warnings.simplefilter('ignore', DeprecationWarning) 
import py2exe
warnings.resetwarnings() 

from gui import FrmMain
from bar import FrmBar
from configGui import FrmConfig
import time

DEFAULT_DIST = "dist"

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
            path = path.replace("\\","\\\\")
            dir = path[path.rindex(self.root)+len(self.root):path.rindex("\\")]
            self.data_files.append((self.dist + dir , [path]))
            
        self.nsisPath = frame.nsisPath
        
        if os.path.exists(self.dist):
            shutil.rmtree(self.dist)


class Setup(object):

    def __init__(self, data):
            
        template = open(os.path.join(os.getcwd(), "templates\\setup.py")).read()
        template %= {"main_script" : data.main_script, "version" : data.version, "company_name" : data.company_name,
                    "copyright" : data.copyright, "name" : data.name, "data_files" : data.data_files, "dist" : data.dist,
                    "includes" : data.includes,  "excludes" : data.excludes, "packages" : data.packages}

        setup = data.root + "\\setup.py"
        f = open(setup, "w")
        f.write(template)
        f.close()
        
        #f = open("log", "w")
                        
        cmd = ["python", setup, "py2exe"]
        p = subprocess.Popen(cmd)
        while p.poll() is None:
            pass


class Nsis(object):
    	
    def __init__(self, data):
            
        files = []
        dir = os.path.join(data.root, data.dist)
        for root, sub_folders, fs in os.walk(dir):
            for file in fs:
                path = os.path.join(root, file)
                files.append(path)
                        
        sorted(files, key=lambda x: (x.count("\\"), x))
        
        data_files = []
        ant_dir = ''
        for file in files:
            file = file.encode('ascii')
            set_dir = file[file.rindex(dir)+len(dir):file.rindex("\\")]
            if set_dir != '' and ant_dir != set_dir:
                data_files.append('*** SetOutPath "$INSTDIR' + set_dir + '" *** ***')
                data_files.append("File " + file + "***")
                ant_dir = set_dir
            else:
                data_files.append("File " + file + "***")							
        
        data.files = str(data_files)[1:-1].replace(",", "").replace("'", "")
        
        template = open(os.path.join(os.getcwd(), "templates\\installer.nsi")).read()
        template %= {"main_script" : data.main_script, "version" : data.version, "company_name" : data.company_name,
                   "copyright" : data.copyright, "name" : data.name, "data_files" : data.data_files, "dist" : data.dist,
                   "includes" : data.includes,  "excludes" : data.excludes, "packages" : data.packages,
                   "files": data.files, "main" : data.main}
        
        template = template.replace("***","\n")
        f = open(data.dist + "\\installer.nsi", "w")
        f.write(template)
        f.close()
                        
        #f = open("log2", "w")            
        
        cmd = [data.nsisPath, data.dist + "\\installer.nsi"]
        p = subprocess.Popen(cmd)
        while p.poll() is None:
            pass
            
        print "\n\nFinished Succefully!"


class FrmConfiguration(FrmConfig):
    
    def __init__(self, parent, config):
        FrmConfig.__init__(self, parent)
        self.parent = parent
        self.config = config

    def btOk_click( self, event ):
        
        path = self.dpNsisPath.GetPath()
        self.config.set("paths", "nsis", path)
        self.parent.nsisPath = path
        
        f = open("config.ini", "w")
        self.config.write(f)
        f.close()
                    
        self.Close()

    def btCancel_click( self, event ):
        self.Close()


class FrmApplication(FrmMain):

    file_name = None
    
    def __init__(self, parent):
        FrmMain.__init__(self, parent)
        
        config = ConfigParser.ConfigParser()
        f = open("config.ini", "r")
        config.readfp(f)
        f.close()
        path = config.get("paths", "nsis")
        if not os.path.exists(path):        
            frmConfig = FrmConfiguration(self, config)
            frmConfig.Show()       
        else:
            self.nsisPath = path
    
    def btGenerate_click( self, event ):
        self.generate()
            
    def lbModules_keyDown( self, event ):
        if event.GetKeyCode() == wx.WXK_DELETE:
            self.delete(self.lbModules)
                    
    def lbDirs_keyDown( self, event ):
        if event.GetKeyCode() == wx.WXK_DELETE:
            self.delete(self.lbDirs)
            
    def btAdd_click( self, event ):
        self.add()
            
    def btAddDir_click( self, event ):
        self.add_dir()
    
    def mnOpen_click( self, event ):
        self.open()
    
    def mnSave_click( self, event ):
        self.save()
            
    def mnSaveAs_click( self, event ):
        self.sav4e_as()
    
    def mnExit_click( self, event ):
        self.exit()
    
    def mnAbout_click( self, event ):
        self.about()
            
    def exit(self):
        self.Close()
        
    def btConfig_click( self, event ):
		self.Config()
        
    def Config(self):
        config = ConfigParser.ConfigParser()
        f = open("config.ini", "r")
        config.readfp(f)
        f.close()
        frmConfig = FrmConfiguration(self, config)
        frmConfig.Show()          
    
    def generate(self):		
        if self.tbAppName.GetValue() != '' and self.fpMainScript.GetPath() != '':
            data = AppData(self)
            Setup(data)
            Nsis(data)
        else:
            wx.MessageBox("You must salect a Main script and a Name for your application", "Warning", style=wx.ICON_EXCLAMATION)

    def add(self):
        self.lbModules.Append(self.tbModule.GetValue())
            
    def save(self):
        if self.file_name is not None:
            path = self.file_name
        else:
            path = self._show_file_dialog()
        if path is not None:
            self._save(path)
            
    def save_as(self):		
        path = self._show_file_dialog()
        if path is not None:
            self._save(path)
            
    def _save(self, path):
        f = open(path, "w")
        data = AppData(self)
        pickle.dump(data, f)
        self.file_name = path
            
    def _show_file_dialog(self):
        path = None
        fd = wx.FileDialog(None, "Select Files", style=wx.SAVE, wildcard="*.py2nsis")
        if fd.ShowModal() == wx.ID_OK:
            path = fd.GetPath()				
            if not path.endswith(".py2nsis"):
                path += ".py2nsis"
        return path
            
    def open(self):
        fd = wx.FileDialog(None, "Select Files", style=wx.OPEN, wildcard="*.py2nsis")
        if fd.ShowModal() == wx.ID_OK:
            path = fd.GetPath()
            f = open(path, "r")
            data = pickle.load(f)
            self.clear()
            self.load(data)
            self.file_name = path
                    
    def clear(self):
            
        self.tbVersion.SetValue("")
        self.tbCompany.SetValue("")
        self.tbCopyright.SetValue("")
        self.tbAppName.SetValue("")		
        self.lbModules.Clear()
        self.fpMainScript.SetPath("")		
        self.lbDirs.Clear()
                    
    def load(self, data):
            
        self.tbVersion.SetValue(data.version)
        self.tbCompany.SetValue(data.company_name)
        self.tbCopyright.SetValue(data.copyright)
        self.tbAppName.SetValue(data.name)
        
        for include in data.includes:
            self.lbModules.Append(include)	
                                
        self.fpMainScript.SetPath(data.main_script)
        
        for file in data.data_files:
            self.lbDirs.Append(file[1][0])
            
            
    def add_dir(self):
        fd = wx.FileDialog(None, "Select Files", style=wx.OPEN | wx.MULTIPLE)
        if fd.ShowModal() == wx.ID_OK:
            paths = fd.GetPaths()
            for path in paths:
                self.lbDirs.Append(path)
    
    def delete(self, listbox):		
        indices = listbox.GetSelections()
        for i in reversed(indices):
            try:
                listbox.Delete(i)
            except:
                pass


class App(wx.App):
    
    def OnInit(self):
        frmApplication = FrmApplication(None)
        frmApplication.Show()
        return True
        

if __name__ == '__main__':

    app = App(0)
    app.MainLoop()
