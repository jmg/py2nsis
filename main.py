# -*- coding: utf-8 -*- 
import wx
import os
import subprocess
import pickle

from distutils.core import setup
import warnings 
warnings.simplefilter('ignore', DeprecationWarning) 
import py2exe
warnings.resetwarnings() 

from gui import FrmMain

class AppData(object):
	
	def __init__(self, frame):
		
		self.version = frame.tbVersion.GetValue()
		self.company_name = frame.tbCompany.GetValue()
		self.copyright = frame.tbCopyright.GetValue()
		self.name = frame.tbAppName.GetValue()
		
		self.includes = []
		for i in range(frame.lbModules.GetCount()):
			self.includes.append(frame.lbModules.GetString(i))		
		
		self.packages = []
		
		self.excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
					'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
					'Tkconstants', 'Tkinter']
					
		self.main_script = frame.fpMainScript.GetPath()
		
		self.data_files = []
		for i in range(frame.lbDirs.GetCount()):
			self.data_files.append(frame.lbDirs.GetString(i))
		

class Setup(object):
	
	def __init__(self, data):
		
		template = open(os.path.join(os.getcwd(), "templates\\setup.py")).read()
		template %= {"main_script" : data.main_script, "version" : data.version, "company_name" : data.company_name,
				   "copyright" : data.copyright, "name" : data.name, "data_files" : data.data_files, 
				   "includes" : data.includes,  "excludes" : data.excludes, "packages" : data.packages}

				
		f = open("setup.py", "w")
		f.write(template)
		f.close()
		
		cmd = ["C:\\Python26\python.exe", "setup.py", "py2exe"]
		p = subprocess.Popen(cmd)
		while p.poll() is None:
			pass
		

class Nsis(object):
	
	def __init__(self, data):
		
		data.files = str(["File " + f + "***" for f in os.listdir(os.path.join(os.getcwd(), "dist"))])[1:-1].replace(",", "").replace("'", "")
		data.main = data.main_script[:-3].split("\\")[-1]
		
		template = open(os.path.join(os.getcwd(), "templates\\installer.nsi")).read()
		template %= {"main_script" : data.main_script, "version" : data.version, "company_name" : data.company_name,
				   "copyright" : data.copyright, "name" : data.name, "data_files" : data.data_files, 
				   "includes" : data.includes,  "excludes" : data.excludes, "packages" : data.packages,
				   "files": data.files, "delete_files": "", "main" : data.main}
		
		template = template.replace("***","\n")
		f = open("dist\\installer.nsi", "w")
		f.write(template)
		f.close()
		
		cmd = ["C:\\Archivos de programa\\NSIS\\makensis.exe", "dist\\installer.nsi"]
		p = subprocess.Popen(cmd)
		while p.poll() is None:
			pass
		
		print "\n\nFinished Succefully!"
		

class FrmApplication(FrmMain):
	
	file_name = None
	
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
		
	def exit(self):
		self.Close()
	
	def generate(self):
		data = AppData(self)
		Setup(data)		
		Nsis(data)
	
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
		fd = wx.FileDialog(None, "Select Files", style=wx.SAVE)
		if fd.ShowModal() == wx.ID_OK:
			path = fd.GetPath()				
			if not path.endswith(".py2nsis"):
				path += ".py2nsis"
		return path
		
	def open(self):
		fd = wx.FileDialog(None, "Select Files", style=wx.OPEN)
		if fd.ShowModal() == wx.ID_OK:
			path = fd.GetPath()
			f = open(path, "r")
			data = pickle.load(f)
			self.load(data)
			self.file_name = path
			
	def load(self, data):
		
		self.tbVersion.SetValue(data.version)
		self.tbCompany.SetValue(data.company_name)
		self.tbCopyright.SetValue(data.copyright)
		self.tbAppName.SetValue(data.name)
		
		for include in data.includes:
			self.lbModules.Append(include)	
					
		self.fpMainScript.SetPath(data.main_script)
		
		for file in data.data_files:
			self.lbDirs.Append(file)
		
		
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
		self.SetTopWindow(frmApplication)
		return True

if __name__ == '__main__':
	
	app = App(0)
	app.MainLoop()
