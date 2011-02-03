# -*- coding: utf-8 -*-
import wx
import os
import pickle
import ConfigParser

from distutils.core import setup

#all the GUI Forms
from Gui.Main import FrmMain
from Gui.Config import FrmConfig
from Gui.About import FrmAbout
from Gui.CustomCode import FrmCustomCode

#all the generators
from Generators.Setup import Setup
from Generators.Nsis import Nsis
from Generators.Data import AppData
from Generators.PyInstaller import PyInstaller

#all the constants
from Lib.Constants import *


class FrmCustomizedCode(FrmCustomCode):
    """
        The Form to add Customized Python Code
    """

    def __init__(self, parent):
        FrmCustomCode.__init__(self, parent)

        iconFile = ICON_FILE
        icon = wx.Icon(iconFile, wx.BITMAP_TYPE_ICO)

        self.SetIcon(icon)
        self.parent = parent
        if hasattr(self.parent, 'custom_code'):
            self.tbCode.SetValue(self.parent.custom_code)

    def btOk_click( self, event ):
        self.parent.custom_code = self.tbCode.GetValue()
        self.Close()

    def btCancel_click( self, event ):
        self.Close()


class FrmConfiguration(FrmConfig):
    """
        The Configuration Form to set the Nsis path
    """

    def __init__(self, parent, config):
        FrmConfig.__init__(self, parent)

        iconFile = ICON_FILE
        icon = wx.Icon(iconFile, wx.BITMAP_TYPE_ICO)

        self.SetIcon(icon)

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
    """
        The Main Form of the Application
    """

    # A dict of modes availables
    modes = { MODES.PYINSTALLER : PyInstaller,
              MODES.PY2EXE : Setup,
            }

    def __init__(self, parent):
        FrmMain.__init__(self, parent)

        iconFile = ICON_FILE
        icon = wx.Icon(iconFile, wx.BITMAP_TYPE_ICO)

        self.SetIcon(icon)

        self.file_name = None

        config = ConfigParser.ConfigParser()
        f = open("config.ini", "r")
        config.readfp(f)
        f.close()
        path = config.get("paths", "nsis")
        #if not exists the path to nsis, show the configuration Form
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
        self.save_as()

    def mnExit_click( self, event ):
        self.exit()

    def mnAbout_click( self, event ):
        self.about()

    def mnAddCustomCode_click( self, event ):
        self.addCustomCode()

    def btPy2exe_click( self, event ):
        self.set_mode(MODES.PY2EXE)

    def btpyInstaller_click( self, event ):
        self.set_mode(MODES.PYINSTALLER)

    def exit(self):
        self.Close()

    def btConfig_click( self, event ):
        self.config()

    def set_mode(self, mode):
        """
            Set the mode of the generation.
            see lib/contants to check the MODES enum
        """
        self.mode = mode

    def about(self):
        """
            Show the about form
        """
        frmAbout = FrmAbout(None)
        frmAbout.Show()

    def config(self):
        """
            Read the config and show the form to edit it.
        """
        config = ConfigParser.ConfigParser()
        f = open("config.ini", "r")
        config.readfp(f)
        f.close()
        frmConfig = FrmConfiguration(self, config)
        frmConfig.Show()

    def generate(self):
        """
            Generate the Executable and the Installer
        """
        if self.tbAppName.GetValue() != '' and self.fpMainScript.GetPath() != '':
            #Generate the data object
            data = AppData(self)

            #Call the Class of the actual mode
            self.modes[self.mode](data)

            #if 'only setup.py' checked don't generate the installer
            if not data.setup:
                Nsis(data)
        else:
            wx.MessageBox("You must salect a Main script and a Name for your application", "Warning", style=wx.ICON_EXCLAMATION)

    def add(self):
        self.lbModules.Append(self.tbModule.GetValue())

    def save(self):
        """
            Save the project to a file
        """
        if self.file_name is not None:
            path = self.file_name
        else:
            path = self._show_file_dialog()
        if path is not None:
            self._save(path)

    def save_as(self):
        """
            Save the project to a file asking for a name
        """
        path = self._show_file_dialog()
        if path is not None:
            self._save(path)

    def _save(self, path):
        """
            A private method that serialize the AppData object obtained
            with the parameters in the Main Form
        """
        f = open(path, "w")
        data = AppData(self)
        pickle.dump(data, f)
        self.file_name = path

    def _show_file_dialog(self):
        """
            Show a file dialog and return the selected path plus '.py2nsis'
        """
        path = None
        fd = wx.FileDialog(None, "Select Files", style=wx.SAVE, wildcard="*.py2nsis")
        if fd.ShowModal() == wx.ID_OK:
            path = fd.GetPath()
            if not path.endswith(".py2nsis"):
                path += ".py2nsis"
        return path

    def open(self):
        """
            Open a project File
        """
        fd = wx.FileDialog(None, "Select Files", style=wx.OPEN, wildcard="*.py2nsis")
        if fd.ShowModal() == wx.ID_OK:
            path = fd.GetPath()
            f = open(path, "r")
            data = pickle.load(f)
            self.clear()
            self.load(data)
            self.file_name = path

    def clear(self):
        """
            Clear the Form
        """
        self.tbVersion.SetValue("")
        self.tbCompany.SetValue("")
        self.tbCopyright.SetValue("")
        self.tbAppName.SetValue("")
        self.lbModules.Clear()
        self.fpMainScript.SetPath("")
        self.lbDirs.Clear()

    def load(self, data):
        """
            Load the frame attributes from the deserialized AppData object
        """
        self.tbVersion.SetValue(data.version)
        self.tbCompany.SetValue(data.company_name)
        self.tbCopyright.SetValue(data.copyright)
        self.tbAppName.SetValue(data.name)

        for include in data.includes:
            self.lbModules.Append(include)

        self.fpMainScript.SetPath(data.main_script)

        for file in data.data_files:
            self.lbDirs.Append(file[1][0])

        self.fpLogo.SetPath(data.logo)
        self.custom_code = data.custom_code
        self.cbBundle.SetValue(data.bundle)
        self.ckSetup.SetValue(data.setup)

    def addCustomCode(self):
        """
            Show the Custom Code Form
        """
        frmCustomizedCode = FrmCustomizedCode(self)
        frmCustomizedCode.Show()

    def add_dir(self):
        """
            Add a data file to the listbox
        """
        fd = wx.FileDialog(None, "Select Files", style=wx.OPEN | wx.MULTIPLE)
        if fd.ShowModal() == wx.ID_OK:
            paths = fd.GetPaths()
            for path in paths:
                self.lbDirs.Append(path)

    def delete(self, listbox):
        """
            Delete items from a listbox
        """
        indices = listbox.GetSelections()
        for i in reversed(indices):
            try:
                listbox.Delete(i)
            except:
                pass
