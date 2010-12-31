# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class FrmMain
###########################################################################

class FrmMain ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"py2Nsis", pos = wx.DefaultPosition, size = wx.Size( 480,670 ), style = wx.DEFAULT_FRAME_STYLE|wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 480,670 ), wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel8 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText101 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"General", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )
		self.m_staticText101.SetFont( wx.Font( 10, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer20.Add( self.m_staticText101, 0, wx.ALL, 5 )
		
		gSizer1 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Application Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.tbAppName = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.tbAppName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Version", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		gSizer1.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.tbVersion = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.tbVersion, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Copyright", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		gSizer1.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.tbCopyright = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.tbCopyright, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText22 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Company Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		gSizer1.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.tbCompany = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.tbCompany, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.m_staticText221 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Dist Folder (default is /dist)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )
		gSizer1.Add( self.m_staticText221, 0, wx.ALL, 5 )
		
		self.tbDist = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.tbDist, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Bundle Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		gSizer1.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		cbBundleChoices = [ u"1", u"2", u"3" ]
		self.cbBundle = wx.ComboBox( self.m_panel8, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, cbBundleChoices, 0 )
		gSizer1.Add( self.cbBundle, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.ckSetup = wx.CheckBox( self.m_panel8, wx.ID_ANY, u"Generate Only the Setup.py", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.ckSetup, 0, wx.ALL, 5 )
		
		bSizer20.Add( gSizer1, 0, wx.EXPAND|wx.FIXED_MINSIZE, 5 )
		
		self.m_panel8.SetSizer( bSizer20 )
		self.m_panel8.Layout()
		bSizer20.Fit( self.m_panel8 )
		bSizer2.Add( self.m_panel8, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText102 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Main Script", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText102.Wrap( -1 )
		self.m_staticText102.SetFont( wx.Font( 10, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer2.Add( self.m_staticText102, 0, wx.ALL, 5 )
		
		self.fpMainScript = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer2.Add( self.fpMainScript, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText10212 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Logo Icon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10212.Wrap( -1 )
		self.m_staticText10212.SetFont( wx.Font( 10, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer2.Add( self.m_staticText10212, 0, wx.ALL, 5 )
		
		self.fpLogo = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.ico*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer2.Add( self.fpLogo, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel9 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1021 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Aditional Python Modules", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1021.Wrap( -1 )
		self.m_staticText1021.SetFont( wx.Font( 10, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer22.Add( self.m_staticText1021, 0, wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.tbModule = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.tbModule, 0, wx.ALL, 5 )
		
		self.btAdd = wx.Button( self.m_panel9, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btAdd, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer13.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		lbModulesChoices = []
		self.lbModules = wx.ListBox( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbModulesChoices, wx.LB_EXTENDED )
		bSizer13.Add( self.lbModules, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer22.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		self.m_staticText10211 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Static Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10211.Wrap( -1 )
		self.m_staticText10211.SetFont( wx.Font( 10, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer22.Add( self.m_staticText10211, 0, wx.ALL, 5 )
		
		bSizer131 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.btAddDir = wx.Button( self.m_panel9, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.btAddDir, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer131.Add( bSizer41, 0, wx.EXPAND, 5 )
		
		lbDirsChoices = []
		self.lbDirs = wx.ListBox( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbDirsChoices, wx.LB_EXTENDED )
		bSizer131.Add( self.lbDirs, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer22.Add( bSizer131, 1, wx.EXPAND, 5 )
		
		self.m_panel9.SetSizer( bSizer22 )
		self.m_panel9.Layout()
		bSizer22.Fit( self.m_panel9 )
		bSizer2.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.btGenerate = wx.Button( self.m_panel1, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btGenerate.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer2.Add( self.btGenerate, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0|wx.CLIP_CHILDREN )
		self.mnFile = wx.Menu()
		self.mnOpen = wx.MenuItem( self.mnFile, wx.ID_ANY, u"&Open"+ u"\t" + u"Ctrl+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnFile.AppendItem( self.mnOpen )
		
		self.mnSave = wx.MenuItem( self.mnFile, wx.ID_ANY, u"&Save"+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnFile.AppendItem( self.mnSave )
		
		self.mnSaveAs = wx.MenuItem( self.mnFile, wx.ID_ANY, u"Save As...", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnFile.AppendItem( self.mnSaveAs )
		
		self.mnFile.AppendSeparator()
		
		self.mnExit = wx.MenuItem( self.mnFile, wx.ID_ANY, u"&Exit"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnFile.AppendItem( self.mnExit )
		
		self.m_menubar1.Append( self.mnFile, u"&File" ) 
		
		self.mnCode = wx.Menu()
		self.mnAddCode = wx.MenuItem( self.mnCode, wx.ID_ANY, u"&Add Custom Code", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnCode.AppendItem( self.mnAddCode )
		
		self.m_menubar1.Append( self.mnCode, u"&Code" ) 
		
		self.mnConfiguration = wx.Menu()
		self.mnConfig = wx.MenuItem( self.mnConfiguration, wx.ID_ANY, u"&Paths", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnConfiguration.AppendItem( self.mnConfig )
		
		self.m_menubar1.Append( self.mnConfiguration, u"&Configuration" ) 
		
		self.mnHelp = wx.Menu()
		self.mnAbout = wx.MenuItem( self.mnHelp, wx.ID_ANY, u"&About", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnHelp.AppendItem( self.mnAbout )
		
		self.m_menubar1.Append( self.mnHelp, u"&Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btAdd.Bind( wx.EVT_BUTTON, self.btAdd_click )
		self.lbModules.Bind( wx.EVT_KEY_DOWN, self.lbModules_keyDown )
		self.btAddDir.Bind( wx.EVT_BUTTON, self.btAddDir_click )
		self.lbDirs.Bind( wx.EVT_KEY_DOWN, self.lbDirs_keyDown )
		self.btGenerate.Bind( wx.EVT_BUTTON, self.btGenerate_click )
		self.Bind( wx.EVT_MENU, self.mnOpen_click, id = self.mnOpen.GetId() )
		self.Bind( wx.EVT_MENU, self.mnSave_click, id = self.mnSave.GetId() )
		self.Bind( wx.EVT_MENU, self.mnSaveAs_click, id = self.mnSaveAs.GetId() )
		self.Bind( wx.EVT_MENU, self.mnExit_click, id = self.mnExit.GetId() )
		self.Bind( wx.EVT_MENU, self.mnAddCustomCode_click, id = self.mnAddCode.GetId() )
		self.Bind( wx.EVT_MENU, self.btConfig_click, id = self.mnConfig.GetId() )
		self.Bind( wx.EVT_MENU, self.mnAbout_click, id = self.mnAbout.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btAdd_click( self, event ):
		event.Skip()
	
	def lbModules_keyDown( self, event ):
		event.Skip()
	
	def btAddDir_click( self, event ):
		event.Skip()
	
	def lbDirs_keyDown( self, event ):
		event.Skip()
	
	def btGenerate_click( self, event ):
		event.Skip()
	
	def mnOpen_click( self, event ):
		event.Skip()
	
	def mnSave_click( self, event ):
		event.Skip()
	
	def mnSaveAs_click( self, event ):
		event.Skip()
	
	def mnExit_click( self, event ):
		event.Skip()
	
	def mnAddCustomCode_click( self, event ):
		event.Skip()
	
	def btConfig_click( self, event ):
		event.Skip()
	
	def mnAbout_click( self, event ):
		event.Skip()
	

